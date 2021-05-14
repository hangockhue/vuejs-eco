<template>
  <div>
    <v-container>
      <div class="row">
        <div class="col-md-5 col-sm-5 col-xs-12">
          <v-carousel>
            <v-carousel-item
              :src="require('../assets/img/home/slider4.jpg')"
            >
            </v-carousel-item>
            <v-carousel-item
              :src="require('../assets/img/home/slider2.jpg')"
            >
            </v-carousel-item>
            <v-carousel-item
              :src="require('../assets/img/home/slider3.jpg')"
            >
            </v-carousel-item>
            <v-carousel-item
              :src="require('../assets/img/home/slider1.jpg')"
            >
            </v-carousel-item>

          </v-carousel>
        </div>
        <div class="col-md-7 col-sm-7 col-xs-12">
          <div class="pl-6">
            <p class="display-1 mb-0">{{product.name}}</p>
            <v-card-actions class="pa-0">
              <p class="headline font-weight-light pt-3">{{product.price}} ₫
                <!-- <del style="" class="subtitle-1 font-weight-thin">$80.00</del> -->
              </p>
              <v-spacer>

              </v-spacer>

              <!-- <span class="body-2	font-weight-thin"> 25 REVIEWS</span> -->
            </v-card-actions>
            <p class="subtitle-1 font-weight-thin">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl tincidunt eget nullam non. Tincidunt arcu non sodales neque sodales ut etiam. Lectus arcu bibendum at varius vel pharetra. Morbi tristique senectus et netus et malesuada.
            </p>
            <p class="title">Số lượng</p>

            <v-text-field
                v-model.number="quantity"
                outlined
                style="width:100px"
                dense
            ></v-text-field>
            <v-btn class="primary white--text" @click="addToCart()" outlined tile dense><v-icon>mdi-cart</v-icon> Thêm vào giỏ hàng</v-btn>
            <!-- <v-btn class="ml-4" outlined tile>ADD TO WISHLIST</v-btn> -->

          </div>
      </div>
      </div>
      <product-description>

      </product-description>
    </v-container>

  </div>
</template>
<script>
    import SmallCategory from "./scomponents/SmallCategory";
    import ProductDescription from "./scomponents/ProductDescription";
    import {mapState, mapGetters, mapActions } from 'vuex';

    export default {
        props: ["id"],
        components: {
          SmallCategory,
          ProductDescription
        },
        data() {
          return {
            quantity:1
          }
        },
        computed: {
          ...mapState({
            product : state => state.product.product,
          })
        },
        mounted() {
          this.getProduct(this.id);
        },
        methods:{
          ...mapActions('cart' ,['addProductToCart']),
          ...mapActions("product", ['getProduct']),

          addToCart() {
            this.addProductToCart({
              product: this.product,
              quantity: this.quantity
            });
          },
        }
    }
</script>
