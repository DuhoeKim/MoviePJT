<template>
  <div class="container d-flex flex-column justify-content-center" style="height: 100vh;">
    <div class="content d-flex flex-column p-5">
      <h1 class="text-center title">[ {{ movie.title }} ]</h1>
      <div class="button-container mb-3">
        <h2 class="text-center sub-title">리뷰 게시판</h2>
        <button 
          @click="goMovieDetail"
          class="btn btn-lg bg-custom text-white me-3 back"
          >
          돌아가기
        </button>
        <button
          class="btn btn-lg bg-custom text-white write"
          @click="createReview"
        >리뷰 작성</button>
      </div>
      
      <div class="p-5">
        <p v-if="!reviews.length"
          class="text-center"
        > 작성된 리뷰가 없습니다.</p>
        <ReviewList
          v-for="review in reviews"
          :key="review.id"
          :review="review"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'
export default {
  name: "MovieReview",
  components:{
    ReviewList
  },
  data() {
    return{
      movieId: JSON.parse(this.$route.query.data).movieId,
    }
  },
  methods:{
    goMovieDetail(){
      this.$router.push({name: "MovieDetail", query: {data: JSON.stringify({movieId: this.movieId})}})
    },
    createReview() {
      this.$router.push({ name: "CreateReview", query: {data : JSON.stringify({movieId: this.movieId})}})
    }
  },
  computed: {
    movie() {
      return this.$store.state.movieInfo
    },
    reviews() {
      return this.$store.state.reviews
    },
  },
  created() {
    this.$store.commit('SET_REVIEWS', [])
    this.$store.dispatch('getMovieInfo', this.movieId)
    this.$store.dispatch('getMovieReviews', this.movieId)
  }
}
</script>

<style scoped>
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
    box-shadow: 30px 30px rgb(103,42,66);
  }
  .list-content {
    background-color: rgb(103,42,66);
    border-radius: 20px;
  }
  .bg-custom{
    background: rgb(103,42,66);
  }
  .title{
    font-size: 3rem;
    text-shadow: 5px 5px rgb(103,42,66);
  }
  .sub-title{
    font-size: 2.5rem;
    text-shadow: 5px 5px rgb(103,42,66);
  }
  .button-container{
    position: relative;
  }
  .back{
    position: absolute;
    top: 20%;
    left: 0%;
  }
  .write{
    position: absolute;
    top: 20%;
    right: 0%;
  }
  
</style>