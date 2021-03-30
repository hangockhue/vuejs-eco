import axios from "axios";

const Api = axios.create({
    baseURL: 'https://6020a71446f1e4001780348c.mockapi.io/'
});

export default Api;