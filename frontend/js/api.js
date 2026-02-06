/**
 * Aarogya Saathi - Shared API wrapper
 */

const API_BASE = 'http://localhost:8000';

async function apiFetch(path, options = {}) {
    const url = `${API_BASE}${path}`;
    const token = localStorage.getItem('token');

    const headers = {
        'Content-Type': 'application/json',
        ...(token && { 'Authorization': `Bearer ${token}` }),
        ...(options.headers || {}),
    };

    try {
        const res = await fetch(url, { ...options, headers });
        if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: res.statusText }));
            throw new Error(err.detail || `HTTP ${res.status}`);
        }
        return await res.json();
    } catch (err) {
        console.error(`API Error [${path}]:`, err.message);
        throw err;
    }
}

function apiGet(path) {
    return apiFetch(path);
}

function apiPost(path, body) {
    return apiFetch(path, { method: 'POST', body: JSON.stringify(body) });
}

function apiPut(path, body) {
    return apiFetch(path, { method: 'PUT', body: JSON.stringify(body) });
}

function apiDelete(path) {
    return apiFetch(path, { method: 'DELETE' });
}

// Auth helpers
function getParentId() {
    return localStorage.getItem('parent_id');
}

function setParentId(id) {
    localStorage.setItem('parent_id', id);
}

function isLoggedIn() {
    return !!localStorage.getItem('token');
}

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('parent_id');
    localStorage.removeItem('family_name');
    window.location.href = 'index.html';
}

// UI helpers
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    const colors = {
        success: 'bg-green-500',
        error: 'bg-red-500',
        warning: 'bg-yellow-500',
        info: 'bg-indigo-500',
    };
    toast.className = `fixed top-4 right-4 ${colors[type]} text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-opacity duration-300`;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function feelingBadge(feeling) {
    const map = {
        1: { text: 'Good 😊', cls: 'badge-good' },
        2: { text: 'Okay 😐', cls: 'badge-ok' },
        3: { text: 'Not well 😟', cls: 'badge-bad' },
    };
    const f = map[feeling] || { text: 'Unknown', cls: '' };
    return `<span class="badge ${f.cls}">${f.text}</span>`;
}

function formatDate(dateStr) {
    if (!dateStr) return '-';
    const d = new Date(dateStr);
    return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' });
}

function formatDateTime(dateStr) {
    if (!dateStr) return '-';
    const d = new Date(dateStr);
    return d.toLocaleString('en-IN', {
        day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit',
    });
}
