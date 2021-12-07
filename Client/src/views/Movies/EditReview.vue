<template>
  <div class="d-flex align-items-center" style="height: 100vh;">
    <div class="container content p-5">
      <h1 class="">리뷰 수정</h1>
      <form @submit.prevent="editReview">
        <div class="mb-3 text-start">
          <label for="title" class="form-label">Title</label>
          <input v-model="review.title" type="text" class="form-control" id="title" required>
        </div>
        <div class="mb-3 text-start">
          <label for="rank" class="form-label">Rank</label>
          <select v-model="review.rank" id="rank" class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
            <option disabled value="">평점을 선택해 주세요.</option>
            <option :value="0.5">🤍 (0.5)</option>
            <option :value="1">🧡 (1.0)</option>
            <option :value="1.5">🧡🤍 (1.5)</option>
            <option :value="2">🧡🧡 (2.0)</option>
            <option :value="2.5">🧡🧡🤍 (2.5)</option>
            <option :value="3">🧡🧡🧡 (3.0)</option>
            <option :value="3.5">🧡🧡🧡🤍 (3.5)</option>
            <option :value="4">🧡🧡🧡🧡 (4.0)</option>
            <option :value="4.5">🧡🧡🧡🧡🤍 (4.5)</option>
            <option :value="5">🧡🧡🧡🧡🧡 (5.0)</option>
          </select>
        </div>
        <div class="mb-3 text-start">
          <label for="content" class="form-label">Content</label>
          <textarea v-model="review.content" name="" class="form-control" id="content" cols="30" rows="10" required></textarea>
        </div>
        <div class="d-flex justify-content-center">
          <button @click="goReviewDetail" type="button" class="btn btn-lg bg-custom text-white me-5">취소하기</button>
          <button type="submit" class="btn btn-lg bg-custom text-white ">수정하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "EditReview",
  data(){
    return{
      reviewId: JSON.parse(this.$route.query.data).reviewId,
    }
  },
  methods:{
    goReviewDetail(){
      this.$router.push({ name: 'ReviewDetail', query:{data: JSON.stringify({reviewId :this.reviewId, movieId: this.review.movie})}})
    },
    editReview(){
      axios.put(`http://localhost:8000/movies/${this.reviewId}/review/update_delete_comment_create/`,{
        ...this.review,
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(() =>{
          this.goReviewDetail()
        })
        .catch(() =>{
          alert('잘못된 양식입니다. 다시 한 번 확인해주세요.')
          this.$store.dispatch('getReviewDetail', this.reviewId)
        })
    }
  },
  computed:{
    review(){
      return this.$store.state.reviewDetail
    },
  },
  created(){
    this.$store.dispatch('getReviewDetail', this.reviewId)
  },
}
</script>

<style scoped>
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
    box-shadow: 30px 30px rgb(103,42,66);
  }
  .bg-custom{
    background: rgb(103,42,66);
  }
</style>