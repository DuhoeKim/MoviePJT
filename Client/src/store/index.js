import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router/index.js'
import _ from 'lodash'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    accessToken: '',
    movieInfo: {},
    reviews: [],
    reviewDetail: {},
    articles: [],
    articleDetail: {},
    profile: {},
    recommend: [],
    selectedVideo: {},
    randomMovies:[],
  },
  mutations: {
    SET_TOKEN (state, newAccessToken) {
      state.accessToken = newAccessToken
    },
    DELETE_TOKEN (state) {
      state.accessToken = ''
      state.movieInfo= {}
    },
    SET_MOVIES (state, movies) {
      state.movies = movies
    },
    GET_MOVIE_INFO(state, movieInfo){
      state.movieInfo = movieInfo
    },
    DELETE_MOVIE_COMMENT(state, comment){
      state.movieInfo.moviecomment_set.splice(state.movieInfo.moviecomment_set.indexOf(comment), 1)
    },
    EDIT_MOVIE_COMMENT(state, newComment) {
      state.movieInfo.moviecomment_set = state.movieInfo.moviecomment_set.map( comment => {
        if (comment.id === newComment.id) {
          return {
            ...newComment
          } 
        } else {
          return comment
        }
      })

    },
    SET_REVIEWS(state, movieReviews){
      state.reviews = movieReviews
    },
    SET_REVIEW_DETAIL(state, reviewDetail) {
      state.reviewDetail = reviewDetail
    },
    DELETE_REVIEW_COMMENT(state, comment){
      state.reviewDetail.reviewcomment_set.splice(state.reviewDetail.reviewcomment_set.indexOf(comment), 1)
    },
    EDIT_REVIEW_COMMENT(state, newComment) {
      state.reviewDetail.reviewcomment_set = state.reviewDetail.reviewcomment_set.map( comment => {
        if (comment.id === newComment.id) {
          return {
            ...newComment
          } 
        } else {
          return comment
        }
      })

    },
    SET_ARTICLES(state, articles){
      state.articles = articles
    },
    SET_ARTICLE_DETAIL(state, articleDetail){
      state.articleDetail = articleDetail
    },
    DELETE_ARTICLE_COMMENT(state, comment){
      state.articleDetail.comment_set.splice(state.articleDetail.comment_set.indexOf(comment), 1)
    },
    EDIT_ARTICLE_COMMENT(state, newComment){
      state.articleDetail.comment_set = state.articleDetail.comment_set.map( comment => {
        if (comment.id === newComment.id) {
          return {
            ...newComment
          } 
        } else {
          return comment
        }
      })

    },
    SET_PROFILE(state, profile) {
      state.profile = profile
    },
    SET_RECOMMEND_MOVIE(state, recommend){
      state.recommend = recommend
    },
    SET_YOUTUBE_VIDEO(state, selectedVideo){
      state.selectedVideo = selectedVideo
    },
    SET_RANDOM_MOVIES(state, randomMovies){
      state.randomMovies = randomMovies
    },
    REMOVE_LOSER_MOVIE(state, loserIndex){
      state.randomMovies.splice(loserIndex, 1)
    }
  },
  actions: {
    getToken ({ commit }, {username, password }) {
      axios.post('http://localhost:8000/api/token/', { username, password })
      .then(response => {
        localStorage.setItem('accessToken', response.data.access)
        commit('SET_TOKEN', response.data.access)
        })
      },
    getMovieInfo({ commit,dispatch }, movieId){
      axios.get(`http://localhost:8000/movies/${movieId}`)
      .then(response => {
        commit('GET_MOVIE_INFO', response.data)
        dispatch('getMovieVideo', response.data.title)
      })
    },
    getMovies ({ commit,dispatch }){
      axios.get('http://localhost:8000/movies/')
      .then(response => {
        commit('SET_MOVIES', response.data)
        dispatch('startGame')
      })
    },
    deleteMovieComment( { commit, state }, comment){
        axios.delete(`http://localhost:8000/movies/${comment.id}/comment_update_delete/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then(() => {
        commit('DELETE_MOVIE_COMMENT', comment)
      })
    },
    editMovieComment({ commit, state }, newComment){
      axios.put(`http://localhost:8000/movies/${newComment.id}/comment_update_delete/`,{
        ...newComment
      },
      {
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then(()=>{
        commit('EDIT_MOVIE_COMMENT', newComment)
      })
    },
    getMovieReviews({commit}, movieId) {
      axios.get(`http://localhost:8000/movies/${movieId}/review/`)
        .then(response => {
          commit('SET_REVIEWS', response.data)
        })
    },
    getReviewDetail({ commit}, reviewId) {
      axios.get(`http://localhost:8000/movies/${reviewId}/review/detail/`)
        .then(response => {
          commit('SET_REVIEW_DETAIL', response.data)
        })
    },
    deleteReviewComment({ commit, state }, comment) {
      axios.delete(`http://localhost:8000/movies/${comment.id}/review/review_comment_update_delete/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(() => {
          commit('DELETE_REVIEW_COMMENT', comment)
        })
    },
    editReviewComment({commit, state }, newComment){
      axios.put(`http://localhost:8000/movies/${newComment.id}/review/review_comment_update_delete/`,{
        ...newComment
      },
      {
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then(()=>{
        commit('EDIT_REVIEW_COMMENT', newComment)
      })
    },
    deleteReview({ state }, review){
      axios.delete(`http://localhost:8000/movies/${review.id}/review/update_delete_comment_create/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(()=>{
          alert('삭제가 완료되었습니다.')
          router.push({ name : 'MovieReview', query: {data : JSON.stringify({movieId: review.movie })}})
        })
    },
    toggleLike( {commit, state}, info){
      axios.post(`http://localhost:8000/movies/${info.movie}/like/`,{
        ...info,
      },{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(response => {
          commit('GET_MOVIE_INFO', response.data)
        })
    },
    getArticles( { commit }){
      axios.get(`http://localhost:8000/community/articles/`)
        .then( response => {
          commit('SET_ARTICLES', response.data)
        })
    },
    getArticleDetail({ commit }, articleId){
      axios.get(`http://localhost:8000/community/articles/detail/${articleId}/`)
        .then(response => {
          commit('SET_ARTICLE_DETAIL', response.data)
        })
    },
    deleteArticle({state}, articleId){
      axios.delete(`http://localhost:8000/community/articles/${articleId}/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(()=>{
          alert('삭제가 완료되었습니다.')
          router.push({ name : 'Community'})
        })
    },
    deleteArticleComment({ commit, state }, comment){
      axios.delete(`http://localhost:8000/community/comments/${comment.id}/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(()=>{
          commit('DELETE_ARTICLE_COMMENT', comment)
        })
    },
    editArticleComment({commit, state }, newComment){
      axios.put(`http://localhost:8000/community/comments/${newComment.id}/`,{
        ...newComment
      },
      {
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
      .then(()=>{
        commit('EDIT_ARTICLE_COMMENT', newComment)
      })
    },
    getUserInfo({ commit, state }, userId){
      axios.get(`http://localhost:8000/accounts/${userId}/`,{
        headers:{
          Authorization: `Bearer ${state.accessToken}`
        }
      })
        .then(response => {
          commit('SET_PROFILE', response.data)
        })
    },
    getRecommendMovie({commit}, userId){
      axios.get(`http://localhost:8000/movies/${userId}/recommend/`)
        .then(response => {
          commit('SET_RECOMMEND_MOVIE', response.data)
        })
    },
    getMovieVideo({ commit }, movieTitle) {
      const API_URL = process.env.VUE_APP_YOUTUBE_API_URL
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: movieTitle+' 예고편'
      }
      axios.get(API_URL, { params })
        .then(response => {
          const selectedVideo = response.data.items[0]
          commit('SET_YOUTUBE_VIDEO', selectedVideo)
        })
    },
    startGame({ commit, state }){
      const pickedMovies = _.sampleSize(state.movies, 32)
      commit('SET_RANDOM_MOVIES', pickedMovies)
    },
    removeLoserMovie({ commit }, loserIndex){
      commit('REMOVE_LOSER_MOVIE', loserIndex)
    }
  },
  getters: {
    isLogin(state) {
      return !!state.accessToken
    },
    getUserId(state) {
      if(state.accessToken){
        return JSON.parse(atob(state.accessToken.split('.')[1])).user_id
      } else {
        return null
      }
    },
    getUserName(state) {
      if(state.accessToken){
        return JSON.parse(atob(state.accessToken.split('.')[1])).username
      } else {
        return null
      }
    },
    isLikeMovie(state) {
      let flag = false
      if(state.accessToken && state.movieInfo.like_users){
        state.movieInfo.like_users.forEach( user => {
          if(user.username === JSON.parse(atob(state.accessToken.split('.')[1])).username){
            flag=true
          }
        });
      }
      return flag
    }
  },
})
