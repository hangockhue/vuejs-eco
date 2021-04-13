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

const getInformation = ({ commit } , {id, access_token}) => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization' : 'Bearer ' + access_token
        }
    }
    axios.get('http://localhost:8000/user/' + id, config)
    .then(response => {
        commit('SET_INFOR', response.data)
    })
}

const refreshToken = ({ commit },state) => {

}

const logOut = ({commit}) => { 
        commit('LOGOUT_SUCCESS');
}

export default {
    signIn,
    loadUser,
    logOut,
    getInformation,
}