<template>
  <div
    @click="goArticleDetail"
    class="container bottom-line mb-3"
  >
    <div class="list-item d-flex align-items-center p-3">
      <div class="d-flex flex-column">
        <h3>{{ article.title }}</h3>
        <p class="mb-0"> {{ article.username }} | {{ article.created_at.substr(0,10) }} </p>
      </div>
      <p class="ms-auto mt-auto mb-0">댓글 수: {{ article.comment_count }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'articleList',
  props:{
    article: {
      type: Object,
    }
  },
  methods:{
    goArticleDetail(){
      return this.$router.push({ name: "ArticleDetail" , query: {data:JSON.stringify({ articleId: this.article.id })}})
    }
  }
}
</script>

<style scoped>
  .list-item{
    background: rgba(0,0,0,0);
  }
  .list-item:hover{
    background: rgb(155, 113, 113);
    cursor: pointer;
  }
  .bottom-line{
    border-bottom: 2px solid rgb(103,42,66);
  }
</style>