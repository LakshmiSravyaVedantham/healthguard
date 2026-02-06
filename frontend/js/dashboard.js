/**
 * HealthGuard - Dashboard logic
 */

let feelingChart = null;
let adherenceChart = null;

document.addEventListener('DOMContentLoaded', () => {
    if (isLoggedIn() && getParentId()) {
        showDashboard();
    }

    document.getElementById('loginForm').addEventListener('submit', handleLogin);
});

async function handleLogin(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    try {
        const data = await apiPost('/api/auth/login', { email, password });
        localStorage.setItem('token', data.access_token);
        setParentId(data.family_member.parent_id);
        localStorage.setItem('family_name', data.family_member.name);
        showDashboard();
    } catch (err) {
        showToast(err.message, 'error');
    }
}

async function showDashboard() {
    document.getElementById('loginSection').style.display = 'none';
    document.getElementById('dashboardSection').classList.remove('hidden');

    const userBadge = document.getElementById('userBadge');
    const familyName = localStorage.getItem('family_name');
    if (familyName) {
        userBadge.textContent = `Hi, ${familyName}`;
        userBadge.classList.remove('hidden');
    }

    await loadDashboard();
}

async function loadDashboard() {
    const parentId = getParentId();
    if (!parentId) return;

    try {
        const data = await apiGet(`/api/dashboard/${parentId}`);
        renderDashboard(data);
    } catch (err) {
        showToast('Failed to load dashboard: ' + err.message, 'error');
    }
}

function renderDashboard(data) {
    // Parent info
    document.getElementById('parentName').textContent = `${data.parent.name}'s Health Dashboard`;
    document.getElementById('parentInfo').textContent =
        `Age: ${data.parent.age || '-'} | Phone: ${data.parent.phone} | Language: ${data.parent.language}`;

    // Stat cards
    const feelingMap = { 1: '😊 Good', 2: '😐 Okay', 3: '😟 Not well' };
    document.getElementById('statFeeling').textContent =
        data.todays_checkin ? feelingMap[data.todays_checkin.feeling] || '-' : 'No check-in';
    document.getElementById('statAdherence').textContent = `${data.medicine_adherence_7d}%`;
    document.getElementById('statMedicines').textContent =
        `${data.medicines_taken_today}/${data.medicines_total_today}`;
    const activeAlerts = data.recent_alerts.filter(a => !a.resolved).length;
    document.getElementById('statAlerts').textContent = activeAlerts;

    // Feeling chart
    renderFeelingChart(data.checkins_7d);

    // Adherence chart
    renderAdherenceChart(data.medicine_adherence_7d);

    // Alerts list
    renderAlertsList(data.recent_alerts.slice(0, 5));

    // Medicines list
    renderMedicinesList(data.todays_medicines);
}

function renderFeelingChart(checkins) {
    const ctx = document.getElementById('feelingChart').getContext('2d');
    if (feelingChart) feelingChart.destroy();

    const sorted = [...checkins].sort((a, b) => a.checkin_date.localeCompare(b.checkin_date));
    const labels = sorted.map(c => {
        const d = new Date(c.checkin_date);
        return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });
    });
    const values = sorted.map(c => c.feeling);
    const colors = values.map(v => v === 1 ? '#22c55e' : v === 2 ? '#eab308' : '#ef4444');

    feelingChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Feeling',
                data: values,
                backgroundColor: colors,
                borderRadius: 6,
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    min: 0, max: 4,
                    ticks: {
                        stepSize: 1,
                        callback: v => ({ 1: '😊 Good', 2: '😐 OK', 3: '😟 Bad' }[v] || ''),
                    }
                }
            },
            plugins: { legend: { display: false } }
        }
    });
}

function renderAdherenceChart(adherence) {
    const ctx = document.getElementById('adherenceChart').getContext('2d');
    if (adherenceChart) adherenceChart.destroy();

    const taken = adherence;
    const missed = 100 - adherence;

    adherenceChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Taken', 'Missed'],
            datasets: [{
                data: [taken, missed],
                backgroundColor: ['#22c55e', '#f3f4f6'],
                borderWidth: 0,
            }]
        },
        options: {
            responsive: true,
            cutout: '70%',
            plugins: {
                legend: { position: 'bottom' },
            }
        },
        plugins: [{
            id: 'centerText',
            afterDraw(chart) {
                const { ctx: c, chartArea: { width, height, top } } = chart;
                c.save();
                c.font = 'bold 28px sans-serif';
                c.fillStyle = '#4f46e5';
                c.textAlign = 'center';
                c.fillText(`${taken}%`, width / 2, top + height / 2 + 10);
                c.restore();
            }
        }]
    });
}

function renderAlertsList(alerts) {
    const container = document.getElementById('alertsList');
    if (!alerts.length) {
        container.innerHTML = '<p class="text-gray-400 text-center py-4">No recent alerts</p>';
        return;
    }

    container.innerHTML = alerts.map(a => `
        <div class="flex items-center justify-between py-3 border-b border-gray-100 last:border-0">
            <div class="flex items-center gap-3">
                <span class="text-xl">${a.alert_type === 'sos' ? '🆘' : a.alert_type.includes('severe') ? '🚨' : '⚠️'}</span>
                <div>
                    <p class="text-sm font-medium text-gray-800">${a.message}</p>
                    <p class="text-xs text-gray-400">${formatDateTime(a.created_at)}</p>
                </div>
            </div>
            <span class="badge ${a.resolved ? 'badge-resolved' : 'badge-bad'}">
                ${a.resolved ? 'Resolved' : 'Active'}
            </span>
        </div>
    `).join('');
}

function renderMedicinesList(medicines) {
    const container = document.getElementById('medicinesList');
    if (!medicines.length) {
        container.innerHTML = '<p class="text-gray-400 text-center py-4">No medicines scheduled</p>';
        return;
    }

    container.innerHTML = medicines.map(m => `
        <div class="flex items-center justify-between py-3 border-b border-gray-100 last:border-0">
            <div>
                <p class="font-medium text-gray-800">💊 ${m.name}</p>
                ${m.name_telugu ? `<p class="text-sm text-gray-500">${m.name_telugu}</p>` : ''}
            </div>
            <div class="text-right">
                <span class="badge bg-indigo-100 text-indigo-800">${m.time_slot}</span>
                <p class="text-sm text-gray-500 mt-1">${m.dosage || ''}</p>
            </div>
        </div>
    `).join('');
}
