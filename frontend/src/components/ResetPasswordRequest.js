import React, { useState } from 'react';
import axios from 'axios';

const ResetPasswordRequest = () => {
    const [email, setEmail] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/password-reset/', { email });
            console.log(response.data);
        } catch (error) {
            console.error('Password reset request failed:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" placeholder="Enter your email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <button type="submit">Reset Password</button>
        </form>
    );
};

export default ResetPasswordRequest;
