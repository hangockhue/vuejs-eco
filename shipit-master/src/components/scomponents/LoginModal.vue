<template>
    <div :style="isOpen ? 'display:none' : 'display:block'">
        <div class="drawer"></div>
        <div class="my-modal">
        
        <div class="modal-body">
            <div class="form-title text-center">
            <h4>Login</h4>
            </div>
            <div class="d-flex flex-column text-center">
            <form>
                <div class="form-group">
                <input type="email" class="form-control" v-model="username" id="email1" placeholder="Your email address...">
                </div>
                <div class="form-group">
                <input type="password" class="form-control" id="password1" v-model="password" placeholder="Your password...">
                </div>
                <div class="form-group row">
                <div class="col-md-6">
                <button type="button"  @click="signInForm()" class="btn btn-info btn-block btn-round">Login</button>
                </div>
                <div class="col-md-6">
                <button type="button"  @click="test" class="btn btn-danger btn-block btn-round">Thoát</button>
                </div>
                </div>
            </form>
            </div>
        </div>
            <!-- <div id="formContent">
                <div class="fadeIn first">
                <img src="http://danielzawadzki.com/codepen/01/icon.svg" id="icon" alt="User Icon" />
                </div>

                <form>
                <input type="text" id="login" class="fadeIn second" name="login" placeholder="login">
                <input type="text" id="password" class="fadeIn third" name="login" placeholder="password">
                <input type="submit" class="fadeIn fourth" value="Log In">
                </form>
                <div id="formFooter">
                <a class="underlineHover" href="#">Forgot Password?</a>
                </div>

            </div> -->
            
        </div>  
    </div>
   
</template>

<script>
import {mapState, mapActions, mapGetters} from 'vuex';
export default {
    name:'login-modal',
    props: {
        open: Boolean
    },
    data() {
        return{
            username:"",
            password: "",
        }
    },
    computed: {
        isOpen: function(){
            return this.open
        }
    },
    methods: {
        ...mapActions('authencation', ['signIn']),
        signInForm() {
            this.signIn({
                username: this.username,
                password: this.password
            })
            this.$emit('onOpen')
        },
        test() {
            this.$emit('onOpen')
        },
    }

}
</script>

<style scoped>
.drawer{
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    position: absolute;
    background-color: black;
    opacity: 0.3;
    z-index: 999;
}
.my-modal {
    top:30%;
    left:50%;
    position: fixed;
    transform: translate(-50%, -50%);
    width:35%;
    background: white;
    box-shadow: 0px 4px 5px;
    border: none;
    border-radius: 10px 10px 10px 10px;
    z-index: 9999
}
</style>