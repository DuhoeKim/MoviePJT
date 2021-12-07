<template>
  <div class="container mt-5 pt-5">
    <div class="content p-5">
      <h1 class="text-center title">[ {{ movie.title }} ]</h1>
      <h1 class="text-center sub-title">리뷰 게시판</h1>
      <hr>
      <h2>제목: {{ review.title }}</h2>
      <hr>
      <div class="d-flex justify-content-between">
        <div>
          <p class="me-3"> 작성자: {{ review.username }}</p>
          <p>평점: {{ review.rank }}</p>
        </div>
        <div>
          <p> 작성일: {{ review.created_at.substr(0,10)}}</p>
          <p> 마지막 수정일: {{ review.updated_at.substr(0, 10)}} <span v-if="review.created_at.substr(0,19) != review.updated_at.substr(0,19)">(수정됨)</span> </p>
          
        </div>
      </div>
      <hr>
      <div class="pt-5 pb-3">
        <p> {{ review.content}} </p>
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <button @click="goMovieReview" class="btn bg-custom text-white">목록으로</button>
        <div v-if="isLogin && isMine" class="d-flex justify-content-end">
          <button 
            @click="goEditReview"
            class="btn bg-custom text-white me-3"
          >리뷰 수정</button>
          <button 
            @click="deleteReview"
            class="btn bg-custom text-white"
          >리뷰 삭제</button>   
        </div>
      </div>
    </div>

    <div class="content mt-3 p-5">
      <h3>댓글 ( {{ review.reviewcomment_set.length }} )</h3>
      <ReviewCommentItem
        v-for="comment in review.reviewcomment_set"
        :key="comment.id"
        :comment="comment"
      />
      <form 
        v-if="isLogin" 
        @submit.prevent="createReviewComment"
      >
        <div class="d-flex justify-content-between align-items-center mb-2">
          <p class="m-0">댓글작성</p>
          <button class="btn bg-custom text-white ms-3">작성하기</button>
        </div>
        <input type="text" class="form-control" v-model="reviewComment" required>
      </form>
      <div v-else class="d-flex justify-content-center">
        <button 
          class="btn bg-custom text-white p-1 "
          @click="login"
        >댓글작성은 로그인 후 이용가능합니다</button>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewCommentItem from '@/components/ReviewCommentItem'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: "ReviewDetail",
  components:{
    ReviewCommentItem,
  },
  data() {
    return{
      reviewId: JSON.parse(this.$route.query.data).reviewId,
      movieId: JSON.parse(this.$route.query.data).movieId,
      reviewComment: ''
    }
  },
  methods:{
    goMovieReview() {
      this.$router.push({ name: 'MovieReview', query: {data: JSON.stringify({movieId: this.movieId})}})
    },
    goEditReview(){
      this.$router.push( {name: "EditReview", query: {data: JSON.stringify({reviewId: this.reviewId})}})
    },
    deleteReview(){
      this.$store.dispatch('deleteReview', this.review)
    },
    login() {
      const nextroute = {
          name: this.$route.name,
          query: this.$route.query
        }
      this.$router.push({ name: 'Login', query: {next: JSON.stringify(nextroute)}})
    },
    createReviewComment() {
      axios.post(`http://localhost:8000/movies/${this.reviewId}/review/update_delete_comment_create/`, {
        user: this.getUserId,
        content: this.reviewComment
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(() => {
          this.$store.dispatch('getReviewDetail', this.reviewId)
          this.reviewComment = ''
        })
        .catch(() => {
          alert('글자수 제한(200자)를 초과하였습니다.')
        })
    }
  },
  computed: {
    review(){
      return this.$store.state.reviewDetail
    },
    movie() {
      return this.$store.state.movieInfo
    },
    isMine() {
      if(this.getUserId === this.review.user){
        return true
      } else {
        return false
      }
    },
    ...mapGetters([
      'isLogin',
      'getUserId'
    ]),
  },
  created(){
    this.$store.commit('SET_REVIEW_DETAIL', {})
    this.$store.dispatch('getReviewDetail', this.reviewId)
    this.$store.dispatch('getMovieInfo', this.movieId)
  }
}
</script>

<style scoped>
  .content {
    background-color: rgb(39,42,66);
    border-radius: 15px;
  }
  .bg-custom{
    background:rgb(103,42,66);
  }
  .title{
    font-size: 3rem;
    text-shadow: 5px 5px rgb(103,42,66);
  }
  .sub-title{
    font-size: 2.5rem;
    text-shadow: 5px 5px rgb(103,42,66);
  }
</style>