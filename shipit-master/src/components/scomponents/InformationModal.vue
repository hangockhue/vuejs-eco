<template>
    <div :style="isOpen ? 'display:none' : 'display:block'">
        <div class="drawer"></div>
        <div class="my-modal">
        
        <div class="modal-body">
            <div class="form-title text-center">
            <h4>Informtaion</h4>
            </div>
            <div class="d-flex flex-column text-center">
            <form>
                <div class="form-group row">
                    <label class="col-sm-2 col-form-label">Tên :</label>
                    <div class="col-sm-10">
                    <input type="text" class="form-control" :value="userInfor.firstname" >
                    </div>
                </div>
                <div class="form-group row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                    <div class="col-sm-10">
                    <input type="text" readonly class="form-control-plaintext" id="staticEmail" :value="userInfor.email">
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-2 col-form-label">Địa chỉ :</label>
                    <div class="col-sm-10">
                    <input type="text" class="form-control" :value="userInfor.username" >
                    </div>
                </div>
                <div class="form-group row">
                <div class="col-md-6">
                    <button type="button"  class="btn btn-success btn-block btn-round">Lưu</button>
                </div>
                <div class="col-md-6">
                    <button type="button"  @click="test" class="btn btn-danger btn-block btn-round">Thoát</button>
                </div>
                </div>
            </form>
            </div>
            </div>
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
        ...mapState({
            userInfor: state => state.authencation.userInfor
        }),
        isOpen: function(){
            return this.open
        }
    },
    methods: {
        ...mapActions('authencation', ['signIn']),
        
        
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