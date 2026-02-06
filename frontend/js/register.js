/**
 * Aarogya Saathi - Registration forms
 */

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('parentForm').addEventListener('submit', handleParentRegister);
    document.getElementById('familyForm').addEventListener('submit', handleFamilyRegister);
    loadParentsList();
});

async function handleParentRegister(e) {
    e.preventDefault();

    const data = {
        name: document.getElementById('parentName').value,
        phone: document.getElementById('parentPhone').value,
        age: parseInt(document.getElementById('parentAge').value) || null,
        language: document.getElementById('parentLanguage').value,
        health_conditions: document.getElementById('parentConditions').value,
        emergency_contact_phone: document.getElementById('emergencyPhone').value,
    };

    try {
        const result = await apiPost('/api/parents', data);
        document.getElementById('registeredParentId').textContent = result.id;
        document.getElementById('parentResult').classList.remove('hidden');
        document.getElementById('parentForm').reset();
        showToast('Parent registered successfully!');
        loadParentsList();
    } catch (err) {
        showToast(err.message, 'error');
    }
}

async function handleFamilyRegister(e) {
    e.preventDefault();

    const data = {
        name: document.getElementById('familyName').value,
        email: document.getElementById('familyEmail').value,
        password: document.getElementById('familyPassword').value,
        phone: document.getElementById('familyPhone').value,
        parent_id: parseInt(document.getElementById('familyParentId').value),
    };

    try {
        await apiPost('/api/auth/register', data);
        document.getElementById('familyResult').classList.remove('hidden');
        document.getElementById('familyForm').reset();
        showToast('Account created! You can now login.');
    } catch (err) {
        showToast(err.message, 'error');
    }
}

async function loadParentsList() {
    try {
        const parents = await apiGet('/api/parents');
        const container = document.getElementById('parentsList');

        if (!parents.length) {
            container.innerHTML = '<p class="text-gray-400 text-center py-4">No parents registered yet</p>';
            return;
        }

        container.innerHTML = `
            <div class="overflow-x-auto">
                <table class="w-full text-sm">
                    <thead>
                        <tr class="border-b border-gray-200 text-left text-gray-600">
                            <th class="pb-2 font-medium">ID</th>
                            <th class="pb-2 font-medium">Name</th>
                            <th class="pb-2 font-medium">Phone</th>
                            <th class="pb-2 font-medium">Age</th>
                            <th class="pb-2 font-medium">Language</th>
                            <th class="pb-2 font-medium">Conditions</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${parents.map(p => `
                            <tr class="table-row">
                                <td class="py-2 font-bold text-indigo-600">${p.id}</td>
                                <td class="py-2">${p.name}</td>
                                <td class="py-2">${p.phone}</td>
                                <td class="py-2">${p.age || '-'}</td>
                                <td class="py-2 capitalize">${p.language}</td>
                                <td class="py-2">${p.health_conditions || '-'}</td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>
        `;
    } catch (err) {
        document.getElementById('parentsList').innerHTML =
            '<p class="text-red-400 text-center py-4">Failed to load parents</p>';
    }
}
