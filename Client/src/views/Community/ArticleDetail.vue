<template>
  <div class="container mt-5 pt-5">
    <div class="content p-5">
      <h1 class="text-center title" >자유 게시판</h1>
      <hr>
      <h2>제목: {{ article.title }}</h2>
      <hr>
      <div class="d-flex justify-content-between align-items-center">
        <p class="me-3"> 작성자: {{ article.username }}</p>
        <div class="d-flex">
          <p class="me-3"> 작성일: {{ article.created_at.substr(0,10)}}</p>
          <p> 마지막 수정일: {{ article.updated_at.substr(0, 10)}} <span v-if="article.created_at.substr(0,19) != article.updated_at.substr(0,19)">(수정됨)</span> </p>
        </div>
      </div>
      <hr class="mt-0">
      <div class=" pt-5 pb-3">
        <p> {{ article.content}} </p>
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <button @click="goCommuniuty" class="btn bg-custom text-white">목록으로</button>
        <div v-if="isLogin && isMine" class="d-flex justify-content-end">
          <button 
            @click="editArticle"
            class="btn bg-custom text-white me-3"
          >게시글 수정</button>
          <button 
            @click="deleteArticle"
            class="btn bg-custom text-white"
          >게시글 삭제</button>   
        </div>
      </div>
    </div>

    <div class="content mt-3 p-5">
      <h3>댓글 ( {{ article.comment_set.length }} )</h3>
      <AritlceCommentItem
        v-for="comment in article.comment_set"
        :key="comment.id"
        :comment="comment"
      />
      <form 
        v-if="isLogin" 
        @submit.prevent="createArticleComment"   
      >
        <div class="d-flex justify-content-between align-items-center mb-2">
          <p class="m-0">댓글작성</p>
          <button class="d-inline btn bg-custom text-white ms-3">작성하기</button>
        </div>
        <input type="text" class="form-control" v-model="articleComment" required>
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
import { mapGetters } from 'vuex'
import AritlceCommentItem from '@/components/ArticleCommentItem'
import axios from 'axios'

export default {
  name: "ArticleDetail",
  components:{
    AritlceCommentItem
  },
  data() {
    return{
      articleId: JSON.parse(this.$route.query.data).articleId,
      articleComment: ''
    }
  },
  methods:{
    deleteArticle(){
      this.$store.dispatch('deleteArticle', this.articleId)
    },
    editArticle(){
      this.$router.push({ name: 'EditArticle', query: {data: JSON.stringify({articleId: this.articleId})}})
    },
    goCommuniuty(){
      this.$router.push({ name: 'Community'})
    },
    createArticleComment(){
      axios.post(`http://localhost:8000/community/articles/${this.articleId}/comments/`, {
        user: this.getUserId,
        content: this.articleComment
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(() => {
          this.$store.dispatch('getArticleDetail', this.articleId)
          this.articleComment = ''
        })
        .catch(() => {
          alert('글자수 제한(200자)를 초과하였습니다.')
        })
    },
    login() {
      const nextroute = {
          name: this.$route.name,
          query: this.$route.query
        }
      this.$router.push({ name: 'Login', query: {next: JSON.stringify(nextroute)}})
    },
  },
  computed: {
    article(){
      return this.$store.state.articleDetail
    },
    isMine() {
      if(this.getUserId === this.article.user){
        return true
      } else {
        return false
      }
    },
    ...mapGetters([
      'isLogin',
      'getUserId'
    ])
  },
  created() {
    this.$store.commit('SET_ARTICLE_DETAIL', {})
    this.$store.dispatch('getArticleDetail', this.articleId)
  }
}
</script>

<style scoped>
  .content {
    background-color: rgb(39,42,66);
    border-radius: 20px;
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