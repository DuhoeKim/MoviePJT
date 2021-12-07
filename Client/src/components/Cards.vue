<template>
  <div 
    class="col"
    @click="goMovieDetail"
  >
    <div class="card">
      <img :src="imageUrl" class="" alt="" height="500">
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    movie: {
      type: Object
    }
  },
  methods:{
    goMovieDetail() {
      this.$router.push({ name: "MovieDetail", query: {data : JSON.stringify({movieId: this.movie.id})}})
    }
  },
  computed:{
    imageUrl() {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  }
}
</script>

<style scoped>
  .card {
    border-color: rgba(71,42,66,0);
    background: rgba(71,42,66,0);
  }
  img {
    border-radius: 5%;
  }

</style>