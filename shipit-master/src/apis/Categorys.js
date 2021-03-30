  
import Api from "./Api";

const END_POINT = 'categorys';

export default {
    all() {
        return Api.get(END_POINT);
    },
}