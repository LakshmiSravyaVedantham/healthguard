/**
 * Aarogya Saathi - Check-in history & charts
 */

let trendChart = null;

document.addEventListener('DOMContentLoaded', () => {
    const pid = getParentId();
    if (pid) {
        document.getElementById('parentIdInput').value = pid;
        loadCheckins();
    }
});

async function loadCheckins() {
    const parentId = document.getElementById('parentIdInput').value;
    const days = document.getElementById('daysSelect').value;
    if (!parentId) return showToast('Enter a Parent ID', 'warning');

    setParentId(parentId);

    try {
        const [checkins, summary] = await Promise.all([
            apiGet(`/api/parents/${parentId}/checkins?days=${days}`),
            apiGet(`/api/parents/${parentId}/checkins/summary?days=${days}`),
        ]);

        renderSummary(summary);
        renderTrendChart(checkins);
        renderTable(checkins);
    } catch (err) {
        showToast(err.message, 'error');
    }
}

function renderSummary(summary) {
    document.getElementById('totalCheckins').textContent = summary.total_checkins;
    document.getElementById('goodDays').textContent = summary.good_days;
    document.getElementById('okDays').textContent = summary.ok_days;
    document.getElementById('badDays').textContent = summary.bad_days;
}

function renderTrendChart(checkins) {
    const ctx = document.getElementById('trendChart').getContext('2d');
    if (trendChart) trendChart.destroy();

    const sorted = [...checkins].sort((a, b) => a.checkin_date.localeCompare(b.checkin_date));
    const labels = sorted.map(c => {
        const d = new Date(c.checkin_date);
        return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });
    });
    const feelings = sorted.map(c => c.feeling);
    const colors = feelings.map(f => f === 1 ? '#22c55e' : f === 2 ? '#eab308' : '#ef4444');

    trendChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: 'Feeling',
                data: feelings,
                borderColor: '#6366f1',
                backgroundColor: 'rgba(99, 102, 241, 0.1)',
                fill: true,
                tension: 0.3,
                pointBackgroundColor: colors,
                pointRadius: 6,
                pointHoverRadius: 8,
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

function renderTable(checkins) {
    const container = document.getElementById('checkinTable');

    if (!checkins.length) {
        container.innerHTML = '<p class="text-gray-400 text-center py-8">No check-ins found</p>';
        return;
    }

    container.innerHTML = `
        <table class="w-full text-sm">
            <thead>
                <tr class="border-b border-gray-200 text-left text-gray-600">
                    <th class="pb-2 font-medium">Date</th>
                    <th class="pb-2 font-medium">Feeling</th>
                    <th class="pb-2 font-medium">BP</th>
                    <th class="pb-2 font-medium">Sugar</th>
                    <th class="pb-2 font-medium">Pain</th>
                    <th class="pb-2 font-medium">Notes</th>
                </tr>
            </thead>
            <tbody>
                ${checkins.map(c => `
                    <tr class="table-row">
                        <td class="py-2">${formatDate(c.checkin_date)}</td>
                        <td class="py-2">${feelingBadge(c.feeling)}</td>
                        <td class="py-2">${c.bp_systolic && c.bp_diastolic ? `${c.bp_systolic}/${c.bp_diastolic}` : '-'}</td>
                        <td class="py-2">${c.sugar_level || '-'}</td>
                        <td class="py-2">${c.pain_level ? `${c.pain_level}/5` : '-'}</td>
                        <td class="py-2 text-gray-500">${c.notes || '-'}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
    `;
}
