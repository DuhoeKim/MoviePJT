<template>
  <div class="container mt-5 pt-5">
    <h1 class="text-center shadow-effect-2 title">{{getUserName}}의 마이페이지</h1>
    <div class="content p-5 arrow-container">
      <h1 class="mb-3 shadow-effect">My Favorite</h1>
      <h5 v-if="!profile.like_movies.length" class="text-center"> '좋아요'를 표시한 영화가 없습니다. 영화 상세 페이지에서 ♡버튼을 눌러 '좋아요'를 설정할 수 있습니다.</h5>
      
      <div v-else-if="profile.like_movies.length === 1">
        <div class="row row-cols-3 g-4 text-center">
          <div class="col">
          </div>
          <SlideCards
            class="s-scale"
            v-for="(movie, index) in profile.like_movies"
            :key="index"
            :movie="movie"
          />
          <div class="col">
          </div>
        </div>
      </div>

      <div v-else-if="profile.like_movies.length === 2">
        <div class="row g-4 text-center">
          <div class="col-2">
          </div>
          <SlideCards
            class="s-scale col-4"
            v-for="(movie, index) in profile.like_movies"
            :key="index"
            :movie="movie"
          />
          <div class="col-2">
          </div>
        </div>
      </div>

      <div v-else-if="profile.like_movies.length === 3">
        <div class="row row-col-3 g-4 text-center">
          <SlideCards
            class="s-scale"
            v-for="(movie, index) in profile.like_movies"
            :key="index"
            :movie="movie"
          />
        </div>
      </div>
      <!-- Carousel -->
      <div v-else>
        <div class="slide-wrap">
          <div class="row flex-nowrap g-4 text-center like-slide">
            <SlideCards
              class="s-scale"
              v-for="(movie, index) in profile.like_movies"
              :key="index"
              :movie="movie"
            />
          </div>
        </div>
        <div class="d-flex justify-content-between">
        <div v-if="profile.like_movies.length" @click="prev" class="btn text-white scale arrow-left"><font-awesome-icon class="fa-5x arrow-color" icon="chevron-left" /> </div>
        <div v-if="profile.like_movies.length" @click="next" class="btn text-white scale arrow-right"><font-awesome-icon class="fa-5x arrow-color" icon="chevron-right" /></div>
        </div>
      </div>
      <!-- Carousel-end -->
    </div>
    
    <div class="content arrow-container p-5 my-5">
      <h1 class="mb-3 shadow-effect">Recommend</h1>
      <h5 v-if="!recommendedMovies.length" class="text-center"> '좋아요'를 누른 영화를 기반으로 추천영화가 생성됩니다. 영화 상세 페이지에서 ♡버튼을 눌러 '좋아요'를 설정할 수 있습니다. </h5>
      <div class="slide-wrap">
        <div class="row flex-nowrap g-4 text-center recommend-slide">
          <SlideCards
            class="s-scale"
            v-for="(movie, index) in recommendedMovies"
            :key="index"
            :movie="movie"
          />
        </div>
      </div>
      <div class="d-flex justify-content-between">
      <div v-if="profile.like_movies.length" @click="recommendPrev" class="btn text-white scale arrow-left"><font-awesome-icon class="fa-5x arrow-color" icon="chevron-left" /> </div>
      <div v-if="recommendedMovies.length" @click="recommendNext" class="btn text-white scale arrow-right"><font-awesome-icon class="fa-5x arrow-color" icon="chevron-right" /></div>
      </div>
    </div>
  </div>
</template>

<script>
import SlideCards from '@/components/SlideCards'

import { mapGetters } from 'vuex'
export default {
  name: "Profile",
  components:{
    SlideCards,
  },
  data(){
    return{
      nowPoition: 0,
      recommendPosition: 0
    }
  },
  methods:{
    prev(){
      const likeSlide = document.querySelector('.like-slide')
      if (this.nowPoition+1 < 0) {
        likeSlide.style.transform = `translateX(${this.nowPoition+365}px)`
        this.nowPoition = this.nowPoition+365
      } else {
        likeSlide.style.transform = `translateX(${-(365)*(this.profile.like_movies_count-3)}px)`
        this.nowPoition = -365*(this.profile.like_movies_count-3)
      }
    },
    next(){
      const likeSlide = document.querySelector('.like-slide')
      if(this.nowPoition > (-365)*(this.profile.like_movies_count-3)){
        likeSlide.style.transform = `translateX(${this.nowPoition-365}px)`
        this.nowPoition = this.nowPoition-365
      } else {
        likeSlide.style.transform = `translateX(${0}px)`
        this.nowPoition = 0
      }
    },
    recommendPrev(){
      const recommendSlide = document.querySelector('.recommend-slide')
      if (this.recommendPosition+1 < 0) {
        recommendSlide.style.transform = `translateX(${this.recommendPosition+365}px)`
        this.recommendPosition = this.recommendPosition+365
      } else {
        recommendSlide.style.transform = `translateX(${-(365)*(7)}px)`
        this.recommendPosition = -365*(7)
      }
    },
    recommendNext(){
      const recommendSlide = document.querySelector('.recommend-slide')
      if (this.recommendPosition > (-365)*(7)) {
        recommendSlide.style.transform = `translateX(${this.recommendPosition-365}px)`
        this.recommendPosition = this.recommendPosition-365
      } else {
        recommendSlide.style.transform = `translateX(${0}px)`
        this.recommendPosition = 0
      }
    },
  },
  computed:{
    profile(){
      return this.$store.state.profile
    },
    recommendedMovies(){
      return this.$store.state.recommend
    },
    ...mapGetters([
      'getUserName',
      'getUserId'
    ])
  },
  created(){
    this.$store.commit('SET_PROFILE', {})
    this.$store.commit('SET_RECOMMEND_MOVIE', [])
    this.$store.dispatch('getUserInfo', this.getUserId)
    this.$store.dispatch('getRecommendMovie', this.getUserId)
  }
}
</script>

<style scoped>
  .slide-wrap{
    overflow: hidden;
  }
  .like-slide{
    transition: 0.3s ease-out;
  }
  .recommend-slide{
    transition: 0.3s ease-out;
  }
  .s-scale {
    transform: scale(0.8);
    -webkit-transform: scale(0.8);
    -moz-transform: scale(0.8);
    -ms-transform: scale(0.8);
    -o-transform: scale(0.8);
    transition: all 0.3s ease-in-out;  
  }
  .s-scale:hover {
    cursor: pointer;
    z-index: 1;
    transform: scale(0.9);
    -webkit-transform: scale(0.9);
    -moz-transform: scale(0.9);
    -ms-transform: scale(0.9);
    -o-transform: scale(0.9);
  }
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
  }
  .arrow-container{
    position: relative;
  }
  .arrow-left{
    position: absolute;
    top: 40%;
    left: -4rem;
  }
  .arrow-right{
    position: absolute;
    top: 40%;
    right: -4rem;
  }
  .arrow-color {
    color: rgb(103,42,66);
  }
  .shadow-effect{
    text-shadow:5px 5px rgb(135,42,66);
  }
  .shadow-effect-2{
    text-shadow:5px 5px rgb(135,42,66);
  }
  .title{
    font-size: 4rem;
    margin-bottom: 2rem;
  }
</style>