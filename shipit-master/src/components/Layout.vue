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
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Tìm kiếm"
        class="hidden-sm-and-down pl-10 ml-4"
      />
      <v-spacer />
      <div>
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
    <login-modal :open="open" @onOpen= "openModal" ></login-modal>
    <information-modal :open="information" @onOpen= "openInformation"></information-modal>
    <v-content>
      <v-bottom-navigation
        :value="activeBtn"
        color="primary"
        horizontal
      >
        <router-link to="/" class="v-btn">
          <span>Trang chủ</span>
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
    <router-view/>
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
          }),
        },
        mounted() {
          this.getCategorys();
        },
        data() {
          return {
            showModal: false,
            activeBtn: 1,
            on: true,
            login: false,
            open: true,
            information: true,
          }
        },
        methods: {
          ...mapActions('categorys', ['getCategorys']),
          ...mapActions('authencation', ['logOut']),
          ...mapActions('authencation', ['getInformation']),
          openModal() {
              this.open = !this.open
          },
          openInformation() {
            this.information = !this.information;
            // console.log(sta, state.authencation)
            this.getInformation({id : this.$store.state.authencation.id,
                                 access_token : this.$store.state.authencation.token});
          }
        }
    }
</script>
