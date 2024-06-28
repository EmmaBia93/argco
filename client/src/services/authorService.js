import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:5000/api',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  getAuthors() {
    return apiClient.get('/authors');
  },
  getAuthor(id) {
    return apiClient.get(`/authors/${id}`);
  }
};
