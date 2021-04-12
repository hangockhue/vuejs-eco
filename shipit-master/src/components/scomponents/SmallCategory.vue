<template>
    <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover
                  v-slot:default="{ hover }"
                  open-delay="200"
                >
                  <v-card
                    :elevation="hover ? 16 : 2"
                  >
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      :src="require('../../assets/img/home/deal1.jpg')"
                    >
                      <v-card-title>{{category.name}}</v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Baggit, Zara, Fossil</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn
                        class="ma-2"
                        outlined
                        color="info"
                        route :to='"/shop/"+ category.id'
                      >
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
</template>
<script>
export default {
    props: [
      'category'
    ]
}
</script>