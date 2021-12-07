<template>
  <div class="home">
    <div class="main d-flex flex-column">
      <h1 class="fw-bold">Doce Cinema</h1>
      <p class="fs-3 fw-bold"> Search for a movie that will take care of your enjoyment. </p>  
      <input 
        @input="searchMovie"
        class="serach-box mt-5 px-5"
        type="text"
        placeholder="이곳에서 영화를 검색해보세요."
        autofocus
      >
    </div>
    <div class="content mt-5 p-5 movie-cards">
      <div v-if="!searchKeyword" class="row row-cols-1 row-cols-md-4 row-cols-lg-5 g-4 text-center">
        <Cards
          v-for="(movie, index) in movies"
          :key="index"
          :movie="movie"
          class="scale"
        />
      </div>
      <div v-else class="row row-cols-1 row-cols-md-4 row-cols-lg-5 g-4 text-center">
        <Cards
          v-for="(movie, index) in searchList"
          :key="index"
          :movie="movie"
          class="scale"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Cards from '@/components/Cards'

export default {
  name: 'Home',
  components: {
    Cards,
  },
  data() {
    return{
      searchKeyword: '',
      searchList: []
    }
  },
  methods:{
    searchMovie(event){
      this.searchKeyword = event.target.value
    }
  },
  computed:{
    movies() {
      return this.$store.state.movies
    },
  },
  watch:{
    searchKeyword(){
      if(this.searchKeyword.trim()){
        this.searchList = this.movies.filter( movie => {
          return movie.title.match(this.searchKeyword.trim())
        })
      }
    }
  }
}
</script>

<style scoped>
  .serach-box{
    border-radius: 25px;
    height: 50px;
  }
  .serach-box:focus {
    outline: none;
  }
  .content {
    background-color: rgb(39,42,66);
    border-radius: 15px;
  }
  .movie-cards {
    margin-left: 200px;
    margin-right: 200px;
  }
</style>