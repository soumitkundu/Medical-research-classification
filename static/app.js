const { useState } = React;

function MedicalPredictor() {
    const [formData, setFormData] = useState({
        P_incidence: '',
        P_tilt: '',
        L_angle: '',
        S_slope: '',
        P_radius: '',
        S_Degree: ''
    });

    const [errors, setErrors] = useState({});
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [apiError, setApiError] = useState(null);

    const labels = {
        P_incidence: 'P incidence',
        P_tilt: 'P tilt',
        L_angle: 'L angle',
        S_slope: 'S slope',
        P_radius: 'P radius',
        S_Degree: 'S Degree'
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
        // Clear error for this field when user starts typing
        if (errors[name]) {
            setErrors(prev => ({
                ...prev,
                [name]: ''
            }));
        }
        setApiError(null);
    };

    const validateForm = () => {
        const newErrors = {};
        const fields = Object.keys(formData);

        fields.forEach(field => {
            const value = formData[field];
            
            if (value === '' || value === null || value === undefined) {
                newErrors[field] = 'This field is required';
            } else if (isNaN(value)) {
                newErrors[field] = 'Please enter a valid number';
            }
        });

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handlePredict = async (e) => {
        e.preventDefault();
        
        if (!validateForm()) {
            console.log("[v0] Form validation failed");
            return;
        }

        setLoading(true);
        setApiError(null);

        try {
            const payload = {
                P_incidence: parseFloat(formData.P_incidence),
                P_tilt: parseFloat(formData.P_tilt),
                L_angle: parseFloat(formData.L_angle),
                S_slope: parseFloat(formData.S_slope),
                P_radius: parseFloat(formData.P_radius),
                S_Degree: parseFloat(formData.S_Degree)
            };

            console.log("[v0] Sending prediction request with data:", payload);

            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log("[v0] Prediction response received:", data);
            
            setResult(data.prediction);
            setApiError(null);
        } catch (error) {
            console.log("[v0] Error during prediction:", error.message);
            setApiError('Error getting prediction. Please try again.');
            setResult(null);
        } finally {
            setLoading(false);
        }
    };

    const handleClear = () => {
        setFormData({
            P_incidence: '',
            P_tilt: '',
            L_angle: '',
            S_slope: '',
            P_radius: '',
            S_Degree: ''
        });
        setErrors({});
        setResult(null);
        setApiError(null);
        console.log("[v0] Form cleared");
    };

    return (
        <div className="container">
            <div className="header">
                <h1>Medical Research Class Predictor</h1>
                <p>Enter patient measurements to predict the medical research classification</p>
            </div>

            <div className="card">
                <form onSubmit={handlePredict}>
                    <div className="form-grid">
                        {Object.keys(formData).map((field) => (
                            <div key={field} className="form-group">
                                <label htmlFor={field}>{labels[field]}</label>
                                <input
                                    id={field}
                                    type="number"
                                    name={field}
                                    value={formData[field]}
                                    onChange={handleInputChange}
                                    placeholder="Enter numeric value"
                                    step="any"
                                    className={errors[field] ? 'input-error' : ''}
                                />
                                {errors[field] && (
                                    <div className="error-message show">{errors[field]}</div>
                                )}
                            </div>
                        ))}
                    </div>

                    <div className="button-group">
                        <button
                            type="submit"
                            className="predict-btn"
                            disabled={loading}
                        >
                            {loading && <span className="loading-spinner"></span>}
                            {loading ? 'Predicting...' : 'Predict'}
                        </button>
                        <button
                            type="button"
                            className="clear-btn"
                            onClick={handleClear}
                            disabled={loading}
                        >
                            Clear
                        </button>
                    </div>
                </form>

                {apiError && (
                    <div className="error-container show">
                        ⚠️ {apiError}
                    </div>
                )}

                {result !== null && (
                    <div className="result-container show">
                        <div className="result-label">
                            <span className="success-icon">✓</span>Prediction Result
                        </div>
                        <div className="result-value">
                            {result}
                        </div>
                        <div className="result-description">
                            The model has classified this patient into class <strong>{result}</strong> based on the provided measurements.
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

ReactDOM.createRoot(document.getElementById('root')).render(<MedicalPredictor />);
