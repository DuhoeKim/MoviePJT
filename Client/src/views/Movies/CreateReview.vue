<template>
  <div class="d-flex align-items-center" style="height: 100vh;">
    <div class="container content mt-5 p-5">
      <h1 class="">리뷰 작성</h1>
      <form @submit.prevent="postReview">
        <div class="mb-3 text-start">
          <label for="title" class="form-label">Title</label>
          <input type="text" class="form-control" id="title" v-model="title" required>
        </div>
        <div class="mb-3 text-start">
          <label for="rank" class="form-label">Rank</label>
          <select v-model='rank' id="rank" class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
            <option disabled :value="0">평점을 선택해 주세요.</option>
            <option :value="0.5">🤍 (0.5)</option>
            <option :value="1.0">🧡 (1.0)</option>
            <option :value="1.5">🧡🤍 (1.5)</option>
            <option :value="2.0">🧡🧡 (2.0)</option>
            <option :value="2.5">🧡🧡🤍 (2.5)</option>
            <option :value="3.0">🧡🧡🧡 (3.0)</option>
            <option :value="3.5">🧡🧡🧡🤍 (3.5)</option>
            <option :value="4.0">🧡🧡🧡🧡 (4.0)</option>
            <option :value="4.5">🧡🧡🧡🧡🤍 (4.5)</option>
            <option :value="5.0">🧡🧡🧡🧡🧡 (5.0)</option>
          </select>
        </div>
        <div class="mb-3 text-start">
          <label for="content" class="form-label">Content</label>
          <textarea name="" class="form-control" id="content" cols="30" rows="10" v-model="content" required></textarea>
        </div>
        <div class="d-flex justify-content-center">
          <button @click="goMovieReview" type="button" class="btn btn-lg bg-custom text-white me-5">취소하기</button>
          <button  type="submit" class="btn btn-lg bg-custom text-white">작성하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: "CreateReview",
  data(){
    return{
      rank: 0,
      title: '',
      content:'',
      movieId: JSON.parse(this.$route.query.data).movieId,
    }
  },
  methods:{
    goMovieReview() {
      this.$router.push({ name: 'MovieReview', query: {data: JSON.stringify({movieId: this.movieId})}})
    },
    postReview(){
      const newReview = {
        user: this.getUserId,
        movie: this.movieId,
        title: this.title,
        rank: this.rank,
        content: this.content,
      }
      axios.post(`http://localhost:8000/movies/${newReview.movie}/review/create/`, {
        ...newReview
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(response =>{
          this.$router.push({ name: 'ReviewDetail', query: {data : JSON.stringify({reviewId: response.data.id, movieId: this.movieId})} })
        })
        .catch(()=> {
          alert('잘못된 양식입니다. 다시 한 번 확인해주세요.')
          this.title=''
          this.content=''
          this.rank=''
        })
    }
  },
  computed: {
    movie() {
      return this.$store.state.movieInfo
    },
    ...mapGetters([
      'getUserId'
    ]),

  },
  created() {
    this.$store.dispatch('getMovieInfo', this.movieId)
  }
}
</script>

<style scoped>
  .text-start {
    text-align: start;
  }
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
    box-shadow: 30px 30px rgb(103,42,66);
  }
  .bg-custom{
    background: rgb(103,42,66);
  }

</style>