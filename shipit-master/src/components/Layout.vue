<template>
  <v-app id="inspire">
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="primary"
      dark
    >
      <v-toolbar-title
        style="width: 350px"
      >
        <router-link to="/" class="white--text" style="text-decoration: none"><v-icon>mdi-truck</v-icon>&nbsp;Vuejs-Ecomece</router-link>
      </v-toolbar-title>
      <!-- <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Tìm kiếm"
        class="hidden-sm-and-down pl-10 ml-4"
      /> -->
      <!-- <div> -->
        <ejs-autocomplete
          placeholder="Tìm kiếm sản phẩm"
          :dataSource='products'
          :fields="{value: 'name_latin'}"
          v-on:change="test"

        >
        </ejs-autocomplete>
        <v-spacer />
      <!-- </div> -->
      <v-btn v-if="isAuthenticated===true">
        Hi . {{ user }}
      </v-btn>
      <v-btn v-if="isAuthenticated===null" icon @click="openModal">
        <v-icon>mdi-account-arrow-right</v-icon>
      </v-btn>
      <v-btn v-if="isAuthenticated===true" icon @click="openInformation">
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>
      <v-btn v-if="isAuthenticated===true" icon @click="logOut" >
        <v-icon>mdi-account-arrow-left</v-icon>
      </v-btn>
      <v-btn v-on="on" router to="/cart" icon>
        <v-badge
          :content="cartItemCount"
          color="green"
          overlap
        >
          <v-icon>mdi-cart</v-icon>
        </v-badge>
      </v-btn>

      </div>
    </v-app-bar>
    <login-modal :open="authencation.open" @onOpen= "openModal" ></login-modal>
    <information-modal :open="information" @onOpen= "openInformation"></information-modal>
    <v-content>
      <v-bottom-navigation
        :value="activeBtn"
        color="primary"
        horizontal
      >
        <router-link to="/" class="v-btn">
          <span>Trang chủ </span>
        </router-link>
        <v-menu open-on-hover offset-y>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on">
              <span>Danh mục</span>
            </v-btn>
          </template>
          <v-card
            class="mx-auto"
            max-width="344"
            outlined
          >

            <v-list-item
              v-for="(item, index) in categorys"
              :key="index"
              route :to="'/shop/' + item.id"
            >
              <v-list-item-title >{{ item.name }}</v-list-item-title>
            </v-list-item>

          </v-card>
        </v-menu>
        <!-- <router-link to="/product" class="v-btn">
          <span>Product</span>
        </router-link> -->
      </v-bottom-navigation>
    </v-content>

    <router-view @openModal="openModal"/>

    <v-footer
      :padless="true"
    >
      <v-card
        flat
        tile
        width="100%"
        class="secondary white--text text-center"
      >
        <!-- <v-divider></v-divider> -->

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Vuejs Ecomece</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>
<script>
    import { mapGetters , mapState, mapActions } from 'vuex'
    import LoginModal from './scomponents/LoginModal';
    import InformationModal from './scomponents/InformationModal';
    import SmallCart from './scomponents/SmallCart';
    export default {
        components : {
          LoginModal,
          SmallCart,
          InformationModal,
        },
        computed: {
          ...mapGetters('cart', ['cartItemCount']),
          ...mapState({
            categorys: state => state.categorys.categorys,
            isAuthenticated: state => state.authencation.isAuthenticated,
            user: state => state.authencation.user,
            authencation : state => state.authencation,
            products: state => state.product.products,
          }),
        },
        mounted() {
          this.getCategorys();
          this.getProducts();
          this.loadtoken();
        },
        data() {
          return {
            showModal: false,
            activeBtn: 1,
            on: true,
            login: false,
            open: true,
            information: true,
            selected: null,
            dataItem : [ {Id:'Game1', Game: 'Football'},
                          {Id: 'Game2', Game: 'Basketball'},
                          {Id: 'Game3', Game: 'Volleyball'},
                          {Id: 'Game4', Game: 'Baseball'},
                          {Id: 'Game5', Game: 'Badminton'},
                        ],
            dataFields : {value:'Game'}
          };
        },
        methods: {
          ...mapActions('categorys', ['getCategorys']),
          ...mapActions('authencation', ['logOut']),
          ...mapActions('authencation', ['getInformation']),
          ...mapActions('authencation', ['refreshToken']),
          ...mapActions('product', ['getProducts']),
          openModal() {
              console.log(this.$store.state.authencation.open);
              this.$store.state.authencation.open = !this.$store.state.authencation.open
          },
          openInformation() {
            this.information = !this.information;
            // console.log(sta, state.authencation)
            this.getInformation({id : this.$store.state.authencation.id,
                                 access_token : this.$store.state.authencation.token});
          },
          loadtoken () {
            var token = JSON.parse(window.localStorage.getItem("token"))
            if (token != null) {
              this.$store.state.authencation.token = token.access
              this.$store.state.authencation.id = token.refresh
              this.$store.state.authencation.user = token.username
              this.$store.state.authencation.isAuthenticated = true
              this.$store.state.authencation.isLoading = false
              // state.token = response.access;
              // state.user = response.username;
              // state.id = response.id
              // state.isAuthenticated = true;
              // state.isLoading =  false;
            };


          },
          test(e) {
              console.log(e.itemData);
              var id = e.itemData.id
              //redirect(id)
              //this.$router.push({path:`/product/${id}`} );
              // open new link
              window.open(`/product/${id}`, "_self")
          },

          redirect(id) {
            this.$router.push(`/product/${id}`);
          }

        }
    }
</script>

<style>
  @import url(https://cdn.syncfusion.com/ej2/material.css)
</style>

<style>
  .e-ddl.e-input-group.e-control-wrapper .e-input {
      background: white;
  }
</style>
