/**
 * Aarogya Saathi - Alert management
 */

let allAlerts = [];
let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', () => {
    const pid = getParentId();
    if (pid) {
        document.getElementById('parentIdInput').value = pid;
        loadAlerts();
    }
});

async function loadAlerts() {
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Enter a Parent ID', 'warning');

    setParentId(parentId);

    try {
        allAlerts = await apiGet(`/api/parents/${parentId}/alerts`);
        updateCounts();
        renderAlerts();
    } catch (err) {
        showToast(err.message, 'error');
    }
}

function updateCounts() {
    const active = allAlerts.filter(a => !a.resolved).length;
    const resolved = allAlerts.filter(a => a.resolved).length;
    document.getElementById('activeCount').textContent = active;
    document.getElementById('resolvedCount').textContent = resolved;
    document.getElementById('totalCount').textContent = allAlerts.length;
}

function filterAlerts(filter) {
    currentFilter = filter;
    renderAlerts();
}

function renderAlerts() {
    const container = document.getElementById('alertsList');
    let filtered = allAlerts;

    if (currentFilter === 'active') {
        filtered = allAlerts.filter(a => !a.resolved);
    } else if (currentFilter === 'resolved') {
        filtered = allAlerts.filter(a => a.resolved);
    }

    if (!filtered.length) {
        container.innerHTML = `<p class="text-gray-400 text-center py-8">No ${currentFilter} alerts</p>`;
        return;
    }

    container.innerHTML = filtered.map(a => {
        const icon = a.alert_type === 'sos' ? '🆘' :
                     a.alert_type.includes('severe') ? '🚨' :
                     a.alert_type === 'medicine_missed' ? '💊' : '⚠️';

        const typeLabel = {
            'sos': 'SOS',
            'health_severe': 'Health - Urgent',
            'health_bad': 'Health Alert',
            'medicine_missed': 'Medicine Missed',
            'inactivity': 'Inactivity',
        }[a.alert_type] || a.alert_type;

        return `
            <div class="flex items-start justify-between py-4 border-b border-gray-100 last:border-0 ${!a.resolved ? 'bg-red-50/50 -mx-2 px-2 rounded-lg' : ''}">
                <div class="flex items-start gap-3">
                    <span class="text-2xl mt-0.5">${icon}</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-medium text-gray-800">${typeLabel}</span>
                            <span class="badge ${a.resolved ? 'badge-resolved' : 'badge-bad'}">
                                ${a.resolved ? 'Resolved' : 'Active'}
                            </span>
                        </div>
                        <p class="text-sm text-gray-600 mt-1">${a.message}</p>
                        <p class="text-xs text-gray-400 mt-1">
                            ${formatDateTime(a.created_at)}
                            ${a.resolved_at ? ` | Resolved: ${formatDateTime(a.resolved_at)}` : ''}
                        </p>
                    </div>
                </div>
                ${!a.resolved ? `
                    <button onclick="resolveAlert(${a.id})" class="btn-success text-sm whitespace-nowrap">
                        Resolve
                    </button>
                ` : ''}
            </div>
        `;
    }).join('');
}

async function resolveAlert(id) {
    try {
        await apiPut(`/api/alerts/${id}/resolve`);
        showToast('Alert resolved');
        loadAlerts();
    } catch (err) {
        showToast(err.message, 'error');
    }
}
