# translations.py
# Multi-language support for Quantum Computing Simulation
# Supported languages: English, Indonesian, Spanish, Mandarin (中文)

TRANSLATIONS = {
    "English": {
        "lang_code": "en",
        "flag": "🇬🇧",
         
        # Page config
        "page_title": "Quantum Computing Simulation",
        
        # Main title
        "main_title": " Interactive Quantum Computing Simulation",
        
        # Introduction section
        "intro_header": "ℹ️ What is Quantum Computing?",
        "intro_title": "### ⚛️ Introduction to Quantum Computing",
        "intro_content": """
**Quantum Computing** is a computing paradigm that utilizes quantum mechanical phenomena such as **superposition** and **entanglement**.

#### 🔹 Qubit (Quantum Bit)
Unlike classical bits (0 or 1), **qubits** can exist in **superposition** of both states:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalization)

#### 🔹 Quantum Gates
**Quantum gates** are operations that manipulate qubit states, analogous to classical logic gates but **reversible** and **unitary**.

#### 🔹 Measurement
When measured, a qubit **collapses** to one of the basis states (|0⟩ or |1⟩) with probabilities |α|² and |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Simulation Settings",
        "num_qubits_label": "Number of Qubits:",
        "num_qubits_help": "Select the number of qubits for the quantum system (1-3 qubits)",
        "add_gate_header": "🎛️ Add Quantum Gate",
        "select_gate": "Select Gate:",
        "select_gate_help": "Select the quantum gate to apply",
        "target_qubit": "Target Qubit:",
        "target_qubit_help": "Qubit that will receive the gate",
        "apply_gate_btn": "➕ Apply Gate",
        "gate_applied_success": "✅ {gate_name} applied to Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 CNOT Gate (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Target:",
        "cnot_info": "🔗 **CNOT**: Flip target qubit if control qubit = |1⟩",
        "apply_cnot_btn": "➕ Apply CNOT",
        "cnot_applied_success": "✅ CNOT applied (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reset System",
        "reset_warning": "⚠️ System reset to |0...0⟩",
        
        # Main area
        "state_vector_header": " State Vector Visualization",
        "save_state_vector_btn": "💾 Save State Vector Graph",
        "measurement_header": " Measurement Simulation",
        "shots_label": "Number of Shots:",
        "save_measurement_btn": "💾 Save Measurement Histogram",
        
        # State info
        "state_info_header": " State Information",
        "current_state": "#### 📍 Current State:",
        "circuit_history": "#### 🔧 Circuit History:",
        "no_gates_applied": "No gates applied yet",
        "show_matrix": "📐 Show Gate Matrix",
        "matrix_title": "Matrix",
        
        # Plot labels
        "basis_state_label": "Basis State |x⟩",
        "probability_label": "Probability P(x)",
        "probability_dist_title": "📊 Measurement Probability Distribution",
        "amplitude_label": "Amplitude",
        "amplitude_title": "🌊 Complex Amplitude State Vector",
        "real_label": "Real",
        "imaginary_label": "Imaginary",
        "measurement_result_label": "Measurement Result",
        "frequency_label": "Frequency (from {shots} shots)",
        "histogram_title": "Measurement Histogram ({shots} Shots)",

        
        # Gate descriptions
        "gate_hadamard_desc": "Creates superposition: transforms |0⟩ → (|0⟩ + |1⟩)/√2 and |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Bit flip: swaps |0⟩ ↔ |1⟩ (like classical NOT gate)",
        "gate_pauli_y_desc": "Rotation of π radians on the Y axis of the Bloch sphere",
        "gate_pauli_z_desc": "Phase flip: changes the phase of |1⟩ to -|1⟩",
        "gate_s_desc": "Phase shift π/2: adds phase i to |1⟩",
        "gate_t_desc": "Phase shift π/4: important for universal computation",
        
        # Language selector
        "language_label": "🌐 Language:",
    },
    
    "Indonesia": {
        "lang_code": "id",
        "flag": "🇮🇩",
        
        # Page config
        "page_title": "Simulasi Quantum Computing",
        
        # Main title
        "main_title": " Simulasi Quantum Computing Interaktif",
        
        # Introduction section
        "intro_header": "ℹ️ Apa itu Quantum Computing?",
        "intro_title": "### ⚛️ Pengantar Quantum Computing",
        "intro_content": """
**Quantum Computing** adalah paradigma komputasi yang memanfaatkan fenomena mekanika kuantum seperti **superposisi** dan **entanglement**.

#### 🔹 Qubit (Quantum Bit)
Berbeda dengan bit klasik (0 atau 1), **qubit** dapat berada dalam **superposisi** dari kedua state:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalisasi)

#### 🔹 Quantum Gates
**Gate kuantum** adalah operasi yang memanipulasi state qubit, analog dengan logic gate klasik namun **reversible** dan **unitary**.

#### 🔹 Pengukuran
Saat diukur, qubit **collapse** ke salah satu basis state (|0⟩ atau |1⟩) dengan probabilitas |α|² dan |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Pengaturan Simulasi",
        "num_qubits_label": "Jumlah Qubit:",
        "num_qubits_help": "Pilih jumlah qubit untuk sistem kuantum (1-3 qubit)",
        "add_gate_header": "🎛️ Tambahkan Quantum Gate",
        "select_gate": "Pilih Gate:",
        "select_gate_help": "Pilih quantum gate yang akan diterapkan",
        "target_qubit": "Target Qubit:",
        "target_qubit_help": "Qubit yang akan dikenai gate",
        "apply_gate_btn": "➕ Aplikasikan Gate",
        "gate_applied_success": "✅ {gate_name} diterapkan pada Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 CNOT Gate (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Target:",
        "cnot_info": "🔗 **CNOT**: Flip target qubit jika control qubit = |1⟩",
        "apply_cnot_btn": "➕ Aplikasikan CNOT",
        "cnot_applied_success": "✅ CNOT diterapkan (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reset Sistem",
        "reset_warning": "⚠️ Sistem direset ke |0...0⟩",
        
        # Main area
        "state_vector_header": " Visualisasi State Vector",
        "save_state_vector_btn": "💾 Simpan Grafik State Vector",
        "measurement_header": " Simulasi Pengukuran",
        "shots_label": "Jumlah Shots:",
        "save_measurement_btn": "💾 Simpan Histogram Pengukuran",
        
        # State info
        "state_info_header": " Informasi State",
        "current_state": "#### 📍 State Saat Ini:",
        "circuit_history": "#### 🔧 Riwayat Circuit:",
        "no_gates_applied": "Belum ada gate yang diterapkan",
        "show_matrix": "📐 Tampilkan Matrix Gate",
        "matrix_title": "Matrix",
        
        # Plot labels
        "basis_state_label": "Basis State |x⟩",
        "probability_label": "Probabilitas P(x)",
        "probability_dist_title": "📊 Distribusi Probabilitas Pengukuran",
        "amplitude_label": "Amplitudo",
        "amplitude_title": "🌊 Amplitudo Kompleks State Vector",
        "real_label": "Real",
        "imaginary_label": "Imajiner",
        "measurement_result_label": "Hasil Pengukuran",
        "frequency_label": "Frekuensi (dari {shots} shots)",
        "histogram_title": "Histogram Pengukuran ({shots} Shots)",
        
        
        # Gate descriptions
        "gate_hadamard_desc": "Menciptakan superposisi: mengubah |0⟩ → (|0⟩ + |1⟩)/√2 dan |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Flip bit: menukar |0⟩ ↔ |1⟩ (seperti NOT gate klasik)",
        "gate_pauli_y_desc": "Rotasi π radian pada sumbu Y di Bloch sphere",
        "gate_pauli_z_desc": "Phase flip: mengubah tanda fase |1⟩ menjadi -|1⟩",
        "gate_s_desc": "Phase shift π/2: menambah fase i pada |1⟩",
        "gate_t_desc": "Phase shift π/4: penting untuk komputasi universal",
        
        # Language selector
        "language_label": "🌐 Bahasa:",
    },
    
    "Español": {
        "lang_code": "es",
        "flag": "🇪🇸",
        
        # Page config
        "page_title": "Simulación de Computación Cuántica",
        
        # Main title
        "main_title": " Simulación Interactiva de Computación Cuántica",
        
        # Introduction section
        "intro_header": "ℹ️ ¿Qué es la Computación Cuántica?",
        "intro_title": "### ⚛️ Introducción a la Computación Cuántica",
        "intro_content": """
**La Computación Cuántica** es un paradigma de computación que utiliza fenómenos de la mecánica cuántica como la **superposición** y el **entrelazamiento**.

#### 🔹 Qubit (Bit Cuántico)
A diferencia de los bits clásicos (0 o 1), los **qubits** pueden existir en **superposición** de ambos estados:
- |ψ⟩ = α|0⟩ + β|1⟩
- |α|² + |β|² = 1 (normalización)

#### 🔹 Puertas Cuánticas
Las **puertas cuánticas** son operaciones que manipulan estados de qubits, análogas a las puertas lógicas clásicas pero **reversibles** y **unitarias**.

#### 🔹 Medición
Al medirse, un qubit **colapsa** a uno de los estados base (|0⟩ o |1⟩) con probabilidades |α|² y |β|².
""",
        
        # Sidebar
        "sidebar_settings": "⚙️ Configuración de Simulación",
        "num_qubits_label": "Número de Qubits:",
        "num_qubits_help": "Seleccione el número de qubits para el sistema cuántico (1-3 qubits)",
        "add_gate_header": "🎛️ Añadir Puerta Cuántica",
        "select_gate": "Seleccionar Puerta:",
        "select_gate_help": "Seleccione la puerta cuántica a aplicar",
        "target_qubit": "Qubit Objetivo:",
        "target_qubit_help": "Qubit que recibirá la puerta",
        "apply_gate_btn": "➕ Aplicar Puerta",
        "gate_applied_success": "✅ {gate_name} aplicado a Q{target}",
        
        # CNOT section
        "cnot_header": "🔗 Puerta CNOT (2-Qubit)",
        "control_label": "Control:",
        "target_label": "Objetivo:",
        "cnot_info": "🔗 **CNOT**: Invierte el qubit objetivo si el qubit de control = |1⟩",
        "apply_cnot_btn": "➕ Aplicar CNOT",
        "cnot_applied_success": "✅ CNOT aplicado (C: Q{control}, T: Q{target})",
        
        # Reset
        "reset_btn": "🔄 Reiniciar Sistema",
        "reset_warning": "⚠️ Sistema reiniciado a |0...0⟩",
        
        # Main area
        "state_vector_header": " Visualización del Vector de Estado",
        "save_state_vector_btn": "💾 Guardar Gráfico del Vector de Estado",
        "measurement_header": " Simulación de Medición",
        "shots_label": "Número de Disparos:",
        "save_measurement_btn": "💾 Guardar Histograma de Medición",
        
        # State info
        "state_info_header": " Información del Estado",
        "current_state": "#### 📍 Estado Actual:",
        "circuit_history": "#### 🔧 Historial del Circuito:",
        "no_gates_applied": "Aún no se han aplicado puertas",
        "show_matrix": "📐 Mostrar Matriz de la Puerta",
        "matrix_title": "Matriz",
        
        # Plot labels
        "basis_state_label": "Estado Base |x⟩",
        "probability_label": "Probabilidad P(x)",
        "probability_dist_title": "📊 Distribución de Probabilidad de Medición",
        "amplitude_label": "Amplitud",
        "amplitude_title": "🌊 Vector de Estado de Amplitud Compleja",
        "real_label": "Real",
        "imaginary_label": "Imaginario",
        "measurement_result_label": "Resultado de Medición",
        "frequency_label": "Frecuencia (de {shots} disparos)",
        "histogram_title": "Histograma de Medición ({shots} Disparos)",
        
        
        # Gate descriptions
        "gate_hadamard_desc": "Crea superposición: transforma |0⟩ → (|0⟩ + |1⟩)/√2 y |1⟩ → (|0⟩ - |1⟩)/√2",
        "gate_pauli_x_desc": "Inversión de bit: intercambia |0⟩ ↔ |1⟩ (como puerta NOT clásica)",
        "gate_pauli_y_desc": "Rotación de π radianes en el eje Y de la esfera de Bloch",
        "gate_pauli_z_desc": "Inversión de fase: cambia la fase de |1⟩ a -|1⟩",
        "gate_s_desc": "Desplazamiento de fase π/2: añade fase i a |1⟩",
        "gate_t_desc": "Desplazamiento de fase π/4: importante para computación universal",
        
        # Language selector
        "language_label": "🌐 Idioma:",
    },
}

# Available languages for the selector
AVAILABLE_LANGUAGES = ["English", "Indonesia", "Español",]

def get_text(lang, key, **kwargs):
    """
    Get translated text for a given key.
    Falls back to English if key not found.
    """
    if lang not in TRANSLATIONS:
        lang = "English"
    
    text = TRANSLATIONS[lang].get(key, TRANSLATIONS["English"].get(key, key))
    
    # Format with any provided kwargs
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass
    
    return text

def get_gate_description(lang, gate_name):
    """Get translated gate description"""
    gate_desc_map = {
        "Hadamard (H)": "gate_hadamard_desc",
        "Pauli-X": "gate_pauli_x_desc",
        "Pauli-Y": "gate_pauli_y_desc",
        "Pauli-Z": "gate_pauli_z_desc",
        "S Gate": "gate_s_desc",
        "T Gate": "gate_t_desc",
    }
    
    key = gate_desc_map.get(gate_name, "")
    if key:
        return get_text(lang, key)
    return ""
