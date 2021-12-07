import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ChoiceGame from '../views/ChoiceGame.vue'

// Accounts
import Login from '../views/Accounts/Login.vue'
import Signup from '../views/Accounts/Signup.vue'
import Profile from '../views/Accounts/Profile.vue'
// Movies
import MovieDetail from '../views/Movies/MovieDetail.vue'
import ReviewDetail from '../views/Movies/ReviewDetail.vue'
import MovieReview from '../views/Movies/MovieReview.vue'
import CreateReview from '../views/Movies/CreateReview.vue'
import EditReview from '../views/Movies/EditReview.vue'
// Community
import Community from '../views/Community/Community.vue'
import CreateArticle from '../views/Community/CreateArticle.vue'
import EditArticle from '../views/Community/EditArticle.vue'
import ArticleDetail from '../views/Community/ArticleDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,

  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
    
  },
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/createReview',
    name: 'CreateReview',
    component: CreateReview,
    beforeEnter: (to, from, next) => {
      const accessToken = localStorage.getItem('accessToken')
      if (to.name === 'CreateReview'){
        if(accessToken){
          next()
        } else {
          next({ name: 'Login', query: {next: JSON.stringify(to)}})
        }
      }
    },
  },
  {
    path: '/createArticle',
    name: 'CreateArticle',
    component: CreateArticle,
    beforeEnter: (to, from, next) => {
      const accessToken = localStorage.getItem('accessToken')
      if (to.name === 'CreateArticle'){
        if(accessToken){
          next()
        } else {
          next({ name: 'Login', query: {next: JSON.stringify(to)}})
        }
      }
    },
  },
  {
    path: '/editReview',
    name: 'EditReview',
    component: EditReview,
    beforeEnter: (to, from, next) => {
      const accessToken = localStorage.getItem('accessToken')
      if (to.name === 'EditReview'){
        if(accessToken){
          next()
        } else {
          next({ name: 'Login', query: {next: JSON.stringify(to)}})
        }
      }
    },
  },
  {
    path: '/editarticle',
    name: 'EditArticle',
    component: EditArticle,
    beforeEnter: (to, from, next) => {
      const accessToken = localStorage.getItem('accessToken')
      if (to.name === 'EditArticle'){
        if(accessToken){
          next()
        } else {
          next({ name: 'Login', query: {next: JSON.stringify(to)}})
        }
      }
    },
  },
  {
    path: '/movieReview',
    name: 'MovieReview',
    component: MovieReview
  },
  {
    path: '/revieDetail',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/articleDetail',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/choicegame',
    name: 'ChoiceGame',
    component: ChoiceGame
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem('accessToken')
  if (to.name === 'Login' || to.name === 'Signup') {
    if(accessToken) {
      next({ name: 'Home' })
    }
  }
  next()
})
export default router
