/**
 * HealthGuard - Medicine management with presets & kits
 */

// ============ PRESET MEDICINE DATABASE ============
const PRESETS = [
    // BP
    { cat: 'bp', name: 'Amlodipine', telugu: 'అమ్లోడిపిన్', dosage: '5mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'bp', name: 'Telmisartan', telugu: 'టెల్మిసార్టన్', dosage: '40mg', slot: 'morning', time: '08:00', instr: 'Before breakfast' },
    { cat: 'bp', name: 'Atenolol', telugu: 'అటెనోలాల్', dosage: '50mg', slot: 'morning', time: '08:00', instr: 'Before breakfast' },
    { cat: 'bp', name: 'Losartan', telugu: 'లోసార్టన్', dosage: '50mg', slot: 'morning', time: '08:00', instr: 'With food' },
    { cat: 'bp', name: 'Ramipril', telugu: 'రామిప్రిల్', dosage: '5mg', slot: 'morning', time: '08:00', instr: 'Before food' },
    { cat: 'bp', name: 'Cilnidipine', telugu: 'సిల్నిడిపిన్', dosage: '10mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },

    // Diabetes
    { cat: 'diabetes', name: 'Metformin', telugu: 'మెట్‌ఫార్మిన్', dosage: '500mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'diabetes', name: 'Metformin (Night)', telugu: 'మెట్‌ఫార్మిన్ (రాత్రి)', dosage: '500mg', slot: 'night', time: '21:00', instr: 'After dinner' },
    { cat: 'diabetes', name: 'Glimepiride', telugu: 'గ్లిమెపిరైడ్', dosage: '1mg', slot: 'morning', time: '07:30', instr: 'Before breakfast' },
    { cat: 'diabetes', name: 'Sitagliptin', telugu: 'సిటాగ్లిప్టిన్', dosage: '100mg', slot: 'morning', time: '08:00', instr: 'With food' },
    { cat: 'diabetes', name: 'Voglibose', telugu: 'వోగ్లిబోస్', dosage: '0.3mg', slot: 'morning', time: '07:45', instr: 'Before food' },
    { cat: 'diabetes', name: 'Gliclazide', telugu: 'గ్లిక్లాజైడ్', dosage: '80mg', slot: 'morning', time: '07:30', instr: 'Before breakfast' },

    // Heart
    { cat: 'heart', name: 'Aspirin', telugu: 'ఆస్పిరిన్', dosage: '75mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'heart', name: 'Atorvastatin', telugu: 'అటోర్వాస్టాటిన్', dosage: '10mg', slot: 'night', time: '21:00', instr: 'After dinner' },
    { cat: 'heart', name: 'Rosuvastatin', telugu: 'రోసువాస్టాటిన్', dosage: '10mg', slot: 'night', time: '21:00', instr: 'After dinner' },
    { cat: 'heart', name: 'Clopidogrel', telugu: 'క్లోపిడోగ్రెల్', dosage: '75mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'heart', name: 'Ecosprin', telugu: 'ఎకోస్ప్రిన్', dosage: '75mg', slot: 'afternoon', time: '13:00', instr: 'After lunch' },

    // Bones/Joints
    { cat: 'bones', name: 'Calcium + D3', telugu: 'క్యాల్సియం + డి3', dosage: '500mg', slot: 'afternoon', time: '13:00', instr: 'After lunch' },
    { cat: 'bones', name: 'Calcium + D3 (Night)', telugu: 'క్యాల్సియం (రాత్రి)', dosage: '500mg', slot: 'night', time: '21:00', instr: 'After dinner' },
    { cat: 'bones', name: 'Glucosamine', telugu: 'గ్లూకోసమైన్', dosage: '1500mg', slot: 'morning', time: '08:00', instr: 'With food' },
    { cat: 'bones', name: 'Diclofenac (SOS)', telugu: 'డిక్లోఫెనాక్', dosage: '50mg', slot: 'afternoon', time: '13:00', instr: 'After food, only when pain' },
    { cat: 'bones', name: 'Diacerein', telugu: 'డయాసెరిన్', dosage: '50mg', slot: 'night', time: '21:00', instr: 'After dinner' },

    // Vitamins
    { cat: 'vitamins', name: 'Multivitamin', telugu: 'మల్టీవిటమిన్', dosage: '1 tablet', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'vitamins', name: 'Vitamin B12', telugu: 'విటమిన్ బి12', dosage: '1500mcg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    { cat: 'vitamins', name: 'Vitamin D3', telugu: 'విటమిన్ డి3', dosage: '60000 IU', slot: 'morning', time: '08:00', instr: 'Weekly once, with milk' },
    { cat: 'vitamins', name: 'Iron + Folic Acid', telugu: 'ఐరన్ + ఫోలిక్ ఆసిడ్', dosage: '1 tablet', slot: 'morning', time: '08:00', instr: 'Before breakfast' },
    { cat: 'vitamins', name: 'Omega-3 Fish Oil', telugu: 'ఒమెగా-3', dosage: '1000mg', slot: 'morning', time: '08:00', instr: 'With food' },

    // Stomach
    { cat: 'stomach', name: 'Pantoprazole', telugu: 'పాంటోప్రాజోల్', dosage: '40mg', slot: 'morning', time: '07:30', instr: 'Before breakfast, empty stomach' },
    { cat: 'stomach', name: 'Ranitidine', telugu: 'రానిటిడిన్', dosage: '150mg', slot: 'night', time: '21:00', instr: 'Before dinner' },
    { cat: 'stomach', name: 'Domperidone', telugu: 'డాంపెరిడోన్', dosage: '10mg', slot: 'morning', time: '07:45', instr: 'Before food' },
    { cat: 'stomach', name: 'Isabgol (Fiber)', telugu: 'ఇసబ్గోల్', dosage: '1 spoon', slot: 'night', time: '21:30', instr: 'With warm water, before bed' },

    // Thyroid
    { cat: 'thyroid', name: 'Levothyroxine', telugu: 'లెవోథైరాక్సిన్', dosage: '50mcg', slot: 'morning', time: '06:30', instr: 'Empty stomach, 30 min before food' },
    { cat: 'thyroid', name: 'Levothyroxine 75', telugu: 'లెవోథైరాక్సిన్ 75', dosage: '75mcg', slot: 'morning', time: '06:30', instr: 'Empty stomach, 30 min before food' },
    { cat: 'thyroid', name: 'Levothyroxine 100', telugu: 'లెవోథైరాక్సిన్ 100', dosage: '100mcg', slot: 'morning', time: '06:30', instr: 'Empty stomach, 30 min before food' },
];

// ============ MEDICINE KITS ============
const KITS = {
    bp: [
        { name: 'Amlodipine', telugu: 'అమ్లోడిపిన్', dosage: '5mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
        { name: 'Telmisartan', telugu: 'టెల్మిసార్టన్', dosage: '40mg', slot: 'morning', time: '08:00', instr: 'Before breakfast' },
    ],
    diabetes: [
        { name: 'Metformin', telugu: 'మెట్‌ఫార్మిన్', dosage: '500mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
        { name: 'Metformin', telugu: 'మెట్‌ఫార్మిన్', dosage: '500mg', slot: 'night', time: '21:00', instr: 'After dinner' },
        { name: 'Glimepiride', telugu: 'గ్లిమెపిరైడ్', dosage: '1mg', slot: 'morning', time: '07:30', instr: 'Before breakfast' },
    ],
    cholesterol: [
        { name: 'Atorvastatin', telugu: 'అటోర్వాస్టాటిన్', dosage: '10mg', slot: 'night', time: '21:00', instr: 'After dinner' },
        { name: 'Aspirin', telugu: 'ఆస్పిరిన్', dosage: '75mg', slot: 'morning', time: '08:00', instr: 'After breakfast' },
    ],
    general: [
        { name: 'Calcium + D3', telugu: 'క్యాల్సియం + డి3', dosage: '500mg', slot: 'afternoon', time: '13:00', instr: 'After lunch' },
        { name: 'Multivitamin', telugu: 'మల్టీవిటమిన్', dosage: '1 tablet', slot: 'morning', time: '08:00', instr: 'After breakfast' },
        { name: 'Omega-3 Fish Oil', telugu: 'ఒమెగా-3', dosage: '1000mg', slot: 'morning', time: '08:00', instr: 'With food' },
    ],
};

let currentCategory = 'all';

// ============ INIT ============
document.addEventListener('DOMContentLoaded', () => {
    const pid = getParentId();
    if (pid) {
        document.getElementById('parentIdInput').value = pid;
        loadMedicines();
    }
    document.getElementById('medicineForm').addEventListener('submit', handleAddMedicine);
    renderPresetGrid();
});

// ============ PRESET GRID ============
function renderPresetGrid() {
    const grid = document.getElementById('presetGrid');
    const filtered = currentCategory === 'all' ? PRESETS : PRESETS.filter(p => p.cat === currentCategory);

    grid.innerHTML = filtered.map((p, i) => `
        <button onclick="addPreset(${PRESETS.indexOf(p)})"
            style="background:white; border:1px solid #e5e7eb; border-radius:0.5rem; padding:0.625rem; text-align:left; cursor:pointer; transition:all 0.15s;"
            onmouseover="this.style.borderColor='#6366f1'; this.style.background='#eef2ff'"
            onmouseout="this.style.borderColor='#e5e7eb'; this.style.background='white'">
            <div class="font-medium text-sm text-gray-800">${p.name}</div>
            <div class="text-xs text-gray-500">${p.dosage} · ${p.slot}</div>
            <div class="text-xs text-gray-400 mt-0.5">${p.telugu}</div>
        </button>
    `).join('');
}

function showCategory(cat) {
    currentCategory = cat;
    document.querySelectorAll('.cat-tab').forEach(btn => {
        btn.className = btn.id === `tab-${cat}` ? 'cat-tab btn-primary' : 'cat-tab btn-secondary';
        btn.style.fontSize = '0.75rem';
    });
    renderPresetGrid();
}

// ============ ADD PRESET (one tap) ============
async function addPreset(index) {
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Set Parent ID first', 'warning');

    const p = PRESETS[index];
    try {
        await apiPost(`/api/parents/${parentId}/medicines`, {
            name: p.name,
            name_telugu: p.telugu,
            dosage: p.dosage,
            time_slot: p.slot,
            time_exact: p.time,
            instructions: p.instr,
        });
        showToast(`Added ${p.name}!`);
        loadMedicines();
    } catch (err) {
        showToast(err.message, 'error');
    }
}

// ============ ADD KIT (one click = multiple medicines) ============
async function addKit(kitName) {
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Set Parent ID first', 'warning');

    const kit = KITS[kitName];
    if (!kit) return;

    let added = 0;
    for (const m of kit) {
        try {
            await apiPost(`/api/parents/${parentId}/medicines`, {
                name: m.name,
                name_telugu: m.telugu,
                dosage: m.dosage,
                time_slot: m.slot,
                time_exact: m.time,
                instructions: m.instr,
            });
            added++;
        } catch (err) {
            console.error(`Failed to add ${m.name}:`, err);
        }
    }
    showToast(`${kitName.toUpperCase()} Kit added! (${added} medicines)`);
    loadMedicines();
}

// ============ CUSTOM FORM TOGGLE ============
function toggleCustomForm() {
    const section = document.getElementById('customFormSection');
    const arrow = document.getElementById('customArrow');
    const isHidden = section.classList.contains('hidden');
    section.classList.toggle('hidden');
    arrow.style.transform = isHidden ? 'rotate(90deg)' : 'rotate(0deg)';
}

// ============ LOAD & RENDER ============
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
        container.innerHTML = '<p class="text-gray-400 text-center py-8">No medicines added yet — use the kits above!</p>';
        return;
    }

    const slots = { morning: [], afternoon: [], night: [] };
    medicines.forEach(m => (slots[m.time_slot] || slots.morning).push(m));
    const icons = { morning: '🌅', afternoon: '☀️', night: '🌙' };

    container.innerHTML = Object.entries(slots)
        .filter(([, meds]) => meds.length > 0)
        .map(([slot, meds]) => `
            <div class="mb-5">
                <h4 class="font-semibold text-gray-700 mb-2 capitalize">${icons[slot] || ''} ${slot}</h4>
                ${meds.map(m => `
                    <div class="flex items-center justify-between py-3 px-4 mb-2" style="background:#f9fafb; border-radius:0.5rem;">
                        <div>
                            <span class="font-medium text-gray-800">${m.name}</span>
                            ${m.name_telugu ? `<span class="text-gray-400 text-sm ml-1">(${m.name_telugu})</span>` : ''}
                            <div class="text-xs text-gray-500 mt-0.5">${m.dosage || ''} ${m.instructions ? '· ' + m.instructions : ''}</div>
                        </div>
                        <div class="flex items-center gap-3">
                            ${m.time_exact ? `<span class="text-sm font-mono" style="color:#4f46e5">${m.time_exact}</span>` : ''}
                            <button onclick="deleteMedicine(${m.id})" style="color:#ef4444; background:none; border:none; cursor:pointer; font-size:0.8rem;">✕ Remove</button>
                        </div>
                    </div>
                `).join('')}
            </div>
        `).join('');
}

function renderAdherence(summary) {
    const container = document.getElementById('adherenceSummary');
    const pct = summary.adherence_percent;
    const color = pct >= 80 ? '#22c55e' : pct >= 50 ? '#eab308' : '#ef4444';

    container.innerHTML = `
        <div class="text-center mb-3">
            <div style="font-size:2.5rem; font-weight:700; color:${color}">${pct}%</div>
            <div class="text-sm text-gray-500">Adherence Rate</div>
        </div>
        <div style="background:#e5e7eb; border-radius:9999px; height:8px; overflow:hidden;">
            <div style="background:${color}; height:100%; width:${pct}%; border-radius:9999px; transition:width 0.5s;"></div>
        </div>
        <div class="text-center text-xs text-gray-500 mt-2">${summary.total_taken} of ${summary.total_scheduled} taken</div>
    `;
}

// ============ CUSTOM ADD ============
async function handleAddMedicine(e) {
    e.preventDefault();
    const parentId = document.getElementById('parentIdInput').value;
    if (!parentId) return showToast('Set Parent ID first', 'warning');

    try {
        await apiPost(`/api/parents/${parentId}/medicines`, {
            name: document.getElementById('medName').value,
            name_telugu: document.getElementById('medNameTelugu').value,
            dosage: document.getElementById('medDosage').value,
            time_slot: document.getElementById('medTimeSlot').value,
            time_exact: document.getElementById('medTimeExact').value,
            instructions: document.getElementById('medInstructions').value,
        });
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
