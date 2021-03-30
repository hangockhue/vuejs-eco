import axios from 'axios';

const loadUser = ({ commit }) => {
    
}


const signIn = ({ commit }, {username, password}) => {
    const config = {
        headers: {
            'Content-Type' : 'application/json',
        }
    };
    // Resquest Body
    const body = JSON.stringify({username, password})

    axios.post('http://localhost:8000/signup/', body, config)
        .then(response => {
            commit('LOGIN_SUCCESS', response.data);
            console.log(response.data);
            console.log("Login thanh cong");
        })
        .catch(error => {
            commit('ERROR', error);
            console.log("Login that bai");
        })
}

export default {
    signIn,
    loadUser,
}