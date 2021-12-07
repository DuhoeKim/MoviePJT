<template>
  <div class="d-flex align-items-center" style="height: 100vh;">
    <div class="container content p-5">
      <h1>게시물 수정</h1>
      <form @submit.prevent="">
        <div class="mb-3 text-start">
          <label for="title" class="form-label">Title</label>
          <input type="text" class="form-control" id="title" v-model="article.title" required>
        </div>
        <div class="mb-3 text-start">
          <label for="content" class="form-label">Content</label>
          <textarea name="" class="form-control" id="content" cols="30" rows="10" v-model="article.content" required></textarea>
        </div>
        <div class="d-flex justify-content-center">
          <button @click="goArticleDetail" type="button" class="btn btn-lg bg-custom text-white me-5">취소하기</button>
          <button @click="editArticle" type="submit" class="btn btn-lg bg-custom text-white ">수정하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
 name: 'EditArticle',
 data(){
   return{
     articleId: JSON.parse(this.$route.query.data).articleId
   }
 },
 methods: {
   goArticleDetail(){
     this.$router.push({ name: 'ArticleDetail', query: {data: JSON.stringify({articleId: this.articleId})}})
   },
   editArticle(){
     axios.put(`http://localhost:8000/community/articles/${this.articleId}/`,{
        ...this.article,
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(() =>{
          this.goArticleDetail()
        })
        .catch(() =>{
          alert('잘못된 양식입니다. 다시 한 번 확인해주세요.')
          this.$store.dispatch('getArticleDetail', this.articleId)
        })
   }
 },
 computed:{
   article(){
     return this.$store.state.articleDetail
   }
 },
 created(){
   this.$store.dispatch('getArticleDetail', this.articleId)
 }
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