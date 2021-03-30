
const ADD_TO_CART = (state, {product, quantity}) => {
    let productInCart = state.cart.find(item => {
        return item.product.id === product.id
    });

    if (productInCart) {
        productInCart.quantity += quantity;
        return
    }

    state.cart.push({
        product, 
        quantity
    })
}
const REMOVE_PRODUCT_FROM_CART = (state,product) => {
    state.cart = state.cart.filter(item => {
        return item.product.id != product.id;
    })
}


export default {
    ADD_TO_CART,
    REMOVE_PRODUCT_FROM_CART
}