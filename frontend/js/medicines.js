/**
 * Aarogya Saathi - Medicine management
 */

document.addEventListener('DOMContentLoaded', () => {
    const pid = getParentId();
    if (pid) {
        document.getElementById('parentIdInput').value = pid;
        loadMedicines();
    }
    document.getElementById('medicineForm').addEventListener('submit', handleAddMedicine);
});

async function loadMedicines() {
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Enter a Parent ID', 'warning');

    setParentId(parentId);

    try {
        const [medicines, summary] = await Promise.all([
            apiGet(`/api/parents/${parentId}/medicines`),
            apiGet(`/api/parents/${parentId}/medicine-logs/summary?days=7`),
        ]);
        renderMedicines(medicines);
        renderAdherence(summary);
    } catch (err) {
        showToast(err.message, 'error');
    }
}

function renderMedicines(medicines) {
    const container = document.getElementById('medicinesList');

    if (!medicines.length) {
        container.innerHTML = '<p class="text-gray-400 text-center py-8">No medicines added yet</p>';
        return;
    }

    const slots = { morning: [], afternoon: [], night: [] };
    medicines.forEach(m => {
        const slot = slots[m.time_slot] || slots.morning;
        slot.push(m);
    });

    const slotIcons = { morning: '🌅', afternoon: '☀️', night: '🌙' };

    container.innerHTML = Object.entries(slots)
        .filter(([, meds]) => meds.length > 0)
        .map(([slot, meds]) => `
            <div class="mb-6">
                <h4 class="font-semibold text-gray-700 mb-2 capitalize">
                    ${slotIcons[slot] || ''} ${slot}
                </h4>
                ${meds.map(m => `
                    <div class="flex items-center justify-between py-3 px-4 bg-gray-50 rounded-lg mb-2">
                        <div>
                            <p class="font-medium text-gray-800">${m.name}</p>
                            ${m.name_telugu ? `<p class="text-sm text-gray-500">${m.name_telugu}</p>` : ''}
                            <p class="text-xs text-gray-400">${m.dosage || ''} ${m.instructions ? '• ' + m.instructions : ''}</p>
                        </div>
                        <div class="flex items-center gap-2">
                            ${m.time_exact ? `<span class="text-sm text-indigo-600">${m.time_exact}</span>` : ''}
                            <button onclick="deleteMedicine(${m.id})" class="text-red-400 hover:text-red-600 text-sm">
                                Remove
                            </button>
                        </div>
                    </div>
                `).join('')}
            </div>
        `).join('');
}

function renderAdherence(summary) {
    const container = document.getElementById('adherenceSummary');
    const pct = summary.adherence_percent;
    const color = pct >= 80 ? 'green' : pct >= 50 ? 'yellow' : 'red';

    container.innerHTML = `
        <div class="flex items-center gap-6">
            <div class="text-center">
                <div class="text-3xl font-bold text-${color}-600">${pct}%</div>
                <div class="text-sm text-gray-500">Adherence</div>
            </div>
            <div class="flex-1">
                <div class="w-full bg-gray-200 rounded-full h-3">
                    <div class="bg-${color}-500 h-3 rounded-full transition-all duration-500" style="width: ${pct}%"></div>
                </div>
            </div>
            <div class="text-sm text-gray-600">
                ${summary.total_taken}/${summary.total_scheduled} taken
            </div>
        </div>
    `;
}

async function handleAddMedicine(e) {
    e.preventDefault();
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Set Parent ID first', 'warning');

    const data = {
        name: document.getElementById('medName').value,
        name_telugu: document.getElementById('medNameTelugu').value,
        dosage: document.getElementById('medDosage').value,
        time_slot: document.getElementById('medTimeSlot').value,
        time_exact: document.getElementById('medTimeExact').value,
        instructions: document.getElementById('medInstructions').value,
    };

    try {
        await apiPost(`/api/parents/${parentId}/medicines`, data);
        showToast('Medicine added!');
        document.getElementById('medicineForm').reset();
        loadMedicines();
    } catch (err) {
        showToast(err.message, 'error');
    }
}

async function deleteMedicine(id) {
    if (!confirm('Remove this medicine?')) return;
    try {
        await apiDelete(`/api/medicines/${id}`);
        showToast('Medicine removed');
        loadMedicines();
    } catch (err) {
        showToast(err.message, 'error');
    }
}
