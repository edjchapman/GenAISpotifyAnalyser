import axios from 'axios';
import { getAccessToken } from './authService';

const API_BASE_URL = 'http://localhost:8000/api/';

const apiClient = axios.create({
    baseURL: API_BASE_URL,
});

// Attach Authorization header to all requests
apiClient.interceptors.request.use(
    (config) => {
        const token = getAccessToken();
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default apiClient;
