import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ResetPasswordConfirm = () => {
    const { uidb64, token } = useParams();
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`http://localhost:8000/api/password-reset-confirm/${uidb64}/${token}/`, { password });
            console.log(response.data);
        } catch (error) {
            console.error('Password reset failed:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="password" placeholder="Enter your new password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Set New Password</button>
        </form>
    );
};

export default ResetPasswordConfirm;
