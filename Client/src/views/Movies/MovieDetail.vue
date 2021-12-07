<template>
  <div class="movie-detail mt-5">
    <div class="container">
      <div class="d-flex flex-column pt-5 px-5 mb-2">
        <div class="d-flex content p-5">
          <img class="col-6 align-self-center" :src="imageUrl" alt="" height="" style="border-radius: 5%;">
          <div class="d-flex flex-column justify-content-center p-5">
            <h1 class=""> {{ movieInfo.title}}</h1>
            <h5 class="mb-4">  
              <span> {{ movieInfo.release_date }} | </span>
              <span 
                v-for="(genre, idx) in movieInfo.genres"
                :key="idx"
              > 
                <span v-if="idx === movieInfo.genres.length-1 ">{{ genre }}</span>
                <span v-else>{{ genre }} | </span>
              </span>
            </h5>
            <h4>평점</h4>
            <div class="progress" style="height: 25px;">
              <div class="progress-bar bg-custom fs-4" role="progressbar" :style="{width:  movieInfo.vote_average*10 +'%', height:'100%',}" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">★{{movieInfo.vote_average}}</div>
            </div>
            <h4 class="mt-4">개요</h4>
            <p> {{movieInfo.overview}}</p>
            <div class="d-flex justify-content-center mt-4">
              <button
                v-if="!isLikeMovie"
                @click="toggleLike"
                class="btn bg-custom text-white"
                style="height: 4rem; width: 4rem; border-radius: 70%;"
              >
                <font-awesome-icon :icon="['far', 'heart']" /> {{movieInfo.like_users_count}}</button>
              <button
                v-else
                @click="toggleLike"
                class="btn bg-custom text-white"
                style="height: 4rem; width: 4rem; border-radius: 70%;"
              >
                <font-awesome-icon :icon="['fas', 'heart']" /> {{movieInfo.like_users_count}}</button>
              <button 
                class="btn bg-custom text-white ms-3"
                style="height: 4rem; width: 4rem; border-radius: 70%;"
                @click="goReviews"
              >
              리뷰</button>
            </div>
          </div>
        </div>
    
        <div class="content mt-5 p-5">
          <h3>예고편</h3>
          <iframe
            v-if="videoURI"
            id="player"
            type="text/html"
            width="100%"
            height="650"
            :src="videoURI"
            frameborder="0">
          </iframe>
          <div v-else class="d-flex justify-content-center align-items-center" style="height: 650px" width="100%">
            <font-awesome-icon class="fa-4x me-2" icon="exclamation-circle" />
            <h4>죄송합니다. 현재 요청제한량을 초과하였습니다. 다음에 다시 시도해주세요.</h4> 
          </div>
        </div>

        <div class="content mt-5 p-5">
          <h3 class="text-start">한줄평 ({{movieInfo.moviecomment_set.length}})</h3>
            <div class="movie-comment">
              <CommentItem
                v-for="comment in movieInfo.moviecomment_set"
                :key="comment.id"
                :comment='comment'
              />
              <form v-if="isLogin" @submit.prevent="createMovieComment">
                <div class="d-flex justify-content-between align-items-center mb-2">
                  <p class="m-0">한줄평작성</p>
                  <button class="d-inline btn bg-custom text-white ms-3">작성하기</button>
                </div>
                <input type="text" class="form-control" v-model="movieComment" required>
              </form>
              <div v-else class="d-flex justify-content-center">
                <button 
                  class="btn bg-custom text-white p-1 "
                  @click="login"
                >한줄평작성은 로그인 후 이용가능합니다</button>
              </div>
            </div>
        </div>

      </div>
      <div class="d-flex justify-content-center mt-3">
        <button @click="goHome" class="btn btn-lg bg-custom text-white mb-5">전체 영화목록으로</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentItem from '@/components/CommentItem'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: "MovieDetail",
  components:{
    CommentItem,
  },
  data() {
    return {
      movieId: JSON.parse(this.$route.query.data).movieId,
      movieComment: '',
    }
  },
  methods: {
    toggleLike() {
      if(this.isLogin){
        this.$store.dispatch('toggleLike', {movie: this.movieId, user: this.getUserId})
      } else {
        alert('로그인 후 이용하실 수 있습니다.')
        this.login()
      }
    },
    login() {
      const nextroute = {
        name: this.$route.name,
          query: this.$route.query
        }
      this.$router.push({ name: 'Login', query: {next: JSON.stringify(nextroute)}})
    },
    goHome() {
      this.$router.push({name: 'Home'})
        .then(() => {
          window.scrollTo(0, 0)
        })
    },
    goReviews() {
      this.$router.push({ name: 'MovieReview', query: {data : JSON.stringify({movieId: this.movieId})}})
    },
    getMovieInfo() {
      this.$store.dispatch('getMovieInfo', this.movieId)
    },
    createMovieComment() {
      axios.post(`http://localhost:8000/movies/${this.movieId}/comment_create/`, {
        user: this.getUserId,
        content: this.movieComment
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(() => {
          this.getMovieInfo()
          this.movieComment = ''
        })
        .catch(() => {
          alert('글자수 제한(200자)를 초과하였습니다.')
        })
    }
  },
  computed: {
    imageUrl() {
      return `https://image.tmdb.org/t/p/original${this.movieInfo.poster_path}`
    },
    selectedVideo() {
      return this.$store.state.selectedVideo
    },
    videoURI() {
      if(!_.isEmpty(this.$store.state.selectedVideo)){
        return `http://www.youtube.com/embed/${this.$store.state.selectedVideo.id.videoId}`
      } return ''
    },
    ...mapGetters([
      'isLogin',
      'getUserId',
      'isLikeMovie',
    ]),
    movieInfo() {
      return this.$store.state.movieInfo
    }
  },
  created() {
    this.$store.commit('GET_MOVIE_INFO', {})
    this.$store.commit('SET_YOUTUBE_VIDEO', {})
    this.getMovieInfo()
  }
}
</script>

<style scoped>
  img {
    border-radius: 15px;
  }
  .text-custom{
    color: rgb(135,42,66);
  }
  .border-custom{
    border: 3px solid rgb(135,42,66);
  }
  .bg-custom{
    background-color: rgb(103,42,66);
  }
  .content {
    background-color: rgb(39,42,66);
    border-radius: 15px;
  }
  .custom-progress{
    width:100%;
    height: 25px;
    border-radius: 12.5px;
    background-color: white;
  }
</style>