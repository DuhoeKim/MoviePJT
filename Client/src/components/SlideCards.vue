<template>
  <div 
    class="col"
    @click="goMovieDetail"
  >
    <div class="card">
      <img :src="imageUrl" alt="" height="500">
      <div class="card-body">
        <h4 class="card-title">{{movie.title}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SlideCard",
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
    border-color: rgba(0,0,0,0);
    background: rgb(0, 0, 0, 0);
  }
  .card :hover {
    cursor: pointer;
  }
  img {
    border-radius: 15px;
  }
</style>