
const filterProducts = (state) => (categoryId) => {
    var productsFilter = state.products.filter(
            product => product.category == categoryId
        )
    return productsFilter
}

export default {
    filterProducts
}