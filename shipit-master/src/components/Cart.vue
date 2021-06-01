<template>
  <div>
    <v-container>

      <p class="display-3 font-weight-light	text-center pa-4">GIỎ HÀNG</p>
      <v-row>
        <v-col :cols="12" md="8" sm="12" >
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class="text-center">Sản phẩm</th>
                <th class="text-center">Giá</th>
                <th class="text-center">Số lượng</th>
                <th class="text-center">Tổng</th>
                <th class="text-center"></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(product,i) in cart" :key="i">
                <td>
                  <v-list-item>
                    <v-list-item-avatar>
                      <v-img :src="require('../assets/img/shop/1.jpg')"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title >{{product.product.name}}</v-list-item-title>
                      <v-list-item-subtitle>{{product.subtitle}}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </td>
                <td>${{product.product.price}}</td>
                <td>{{ product.quantity }}</td>
                  <!-- <v-text-field
                    class="pt-10"
                    label="Outlined"
                    style="width: 80px;"
                    single-line
                    outlined
                    :value=product.quantity
                    type="number"
                    min=1
                    v-on:focus="changeMount"
                    
                  ></v-text-field> -->
                  
                
                <td>${{product.product.price*product.quantity}}</td>
                <td><a @click.prevent="removeProductFromCart(product.product)">X</a></td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
        <v-col :cols="12" md="4" sm="12" style="background-color: lightgray">
          <p class="headline">Hóa đơn</p>
          <p class="overline">Phí ship đã được tính toàn và được cộng vào
          </p>
          <v-simple-table>
            <template v-slot:default>
              <tbody>
                <tr>
                  <v-text-field
                    class="col-12"
                    v-model="name"
                    label="Tên"
                    required
                  ></v-text-field></tr>
                 <tr>
                  <v-text-field
                    class="col-12"
                    v-model="address"
                    label="Địa chỉ"
                    required
                  ></v-text-field></tr>
                 <tr>
                  <v-text-field
                    class="col-12"
                    v-model="numberphone"
                    label="Số điện thoại"
                    required
                  ></v-text-field></tr>
                <!-- <tr>
                    <input
                      class="col-12 mx-center"
                      single-line
                      v-model="name"
                      :rules="nameRules"
                      placeholder="Tên"
                      required
                      v-bind:id="name"
                    />
                  </tr> -->
                   <!-- <tr>
                    <input
                      class="col-12 mx-center"
                      single-line
                      v-model="address"
                      :rules="nameRules"
                      placeholder="Địa chỉ"
                      required
                      v-bind:id="name"
                    
                    />
                  </tr> -->
                   <!-- <tr>
                    <input
                      class="col-12 mx-center"
                      single-line
                      v-model="numberphone"
                      :rules="nameRules"
                      placeholder="Số điện thoại"
                      required
                      v-bind:id="name"
                    
                    />
                  </tr> -->

              <tr>
                <td>Tổng đơn hàng</td>
                <td class="text-right" style="width: 150px;">{{cartTotalPrice}} ₫</td>
              </tr>
              <tr>
                <td>VAT</td>
                <td class="text-right" style="width: 150px;">{{ 0.1*cartTotalPrice }}</td>
              </tr>
              <tr>
                <td>Tổng</td>
                <td class="text-right" style="width: 150px;"><b>{{cartTotalPrice + 0.1*cartTotalPrice}} ₫</b></td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
          <div class="text-center">
            <v-btn class="primary white--text mt-5" @click="orderAction(), snackbar = true" outlined>Tiến hành đặt hàng</v-btn>
          </div>
        </v-col>
      </v-row>
      <div class="text-center">
        <v-snackbar
          color="success"
          v-model="snackbar"
          :timeout="timeout"
          right
          top
        >
          {{ text }}

          <template v-slot:action="{ attrs }">
            <v-btn
              color="blue"
              text
              v-bind="attrs"
              @click="snackbar = false"
            >
              Close
            </v-btn>
          </template>
        </v-snackbar>
      </div>
    </v-container>
    <!-- <v-card  class="accent" >
      <v-container>
        <v-row no-gutters>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row >
              <v-col class="col-12 col-sm-3 pr-4 hidden-sm-only" align="right">
                <v-icon class="display-2">mdi-truck</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">FREE SHIPPING & RETURN</h3>
                <p class="font-weight-thin">Free Shipping over $300</p>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row >
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-cash-usd</v-icon>
              </v-col>
              <v-col  class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">MONEY BACK GUARANTEE</h3>
                <p class="font-weight-thin">30 Days Money Back Guarantee</p>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-headset</v-icon>
              </v-col>
              <v-col  class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">020-800-456-747</h3>
                <p class="font-weight-thin">24/7 Available Support</p>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-card> -->
  </div>
</template>
<script>
    import {mapState, mapActions, mapGetters} from 'vuex';
    export default {
        computed: {
          ...mapState({
            cart: state => state.cart.cart
          }),
          ...mapGetters('cart',['cartTotalPrice']),
        },
        methods: {
          ...mapActions("cart" , ['removeProductFromCart']),
          ...mapActions("cart" , ['addOrderToServer']),
          changeMount: function(evt) {
              console.log(evt)
          },
          orderAction() {
              console.log((this.cartTotalPrice + 10));
              console.log(this.name);
              console.log(this.numberphone);
              console.log(this.address);
              this.addOrderToServer();

          }
          
        },
        data: () => ({
            snackbar: false,
            text: "Đơn hàng của bạn đạt thành công",
            timeout: 2000,
            name: '',
            numberphone: '',
            address: '',
            rating: 4.5,
            breadcrums: [
                {
                    text: 'Home',
                    disabled: false,
                    href: 'breadcrumbs_home',
                },
                {
                    text: 'Clothing',
                    disabled: false,
                    href: 'breadcrumbs_clothing',
                },
                {
                    text: 'T-Shirts',
                    disabled: true,
                    href: 'breadcrumbs_shirts',
                },
            ],
    })}
</script>
