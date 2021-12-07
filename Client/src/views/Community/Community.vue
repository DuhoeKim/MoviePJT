<template>
<div class="container d-flex flex-column justify-content-center" style="height: 100vh;">
    <div class="content d-flex flex-column p-5">
      <div class="button-container mb-3">
        <h1 class="text-center title">자유 게시판</h1>
        <button
          @click="goHome"
          class="btn btn-lg bg-custom text-white me-3 back"
        >홈으로 돌아가기</button>

        <button
          @click="createArticle"
          class="btn btn-lg bg-custom text-white write"  
        >게시물 작성</button>
      </div>
      <div class="p-5">
        <p v-if="!articles.length"
          class="text-center"
        > 작성된 게시물이 없습니다.</p>
        <ArticleList
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'Comuunity',
  components:{
    ArticleList,
  },
  methods: {
    createArticle(){
      this.$router.push({ name: 'CreateArticle' })
    },
    goHome(){
      this.$router.push({name: 'Home'})
    }
  },
  computed: {
    articles(){
      return this.$store.state.articles
    }
  },
  created() {
    this.$store.dispatch('getArticles')
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