import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Shop from '@/components/Shop'
import Product from '@/components/Product'
import Post from '@/components/Post'
import Cart from '@/components/Cart'
import Layout from '@/components/Layout'
import Search from '@/components/Search'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Layout,
      children:[
        {
          path:'/',
          component:Home,
          name:'Home'
        },
        {
          path:'/shop/:id',
          component:Shop,
          name:'Shop',
          props: true
        },
        {
          path:'search',
          component: Search,
          name: 'Search'
        },
        {
          path:'/product/:id',
          component:Product,
          name:'Product',
          props: true
        },
        {
          path:'/post',
          component:Post,
          name:'Post'
        },
        {
          path:'/cart',
          component:Cart,
          name:'Cart',
          props: true
        }
      ]

    }
  ],
    mode:'history'
},

  )
