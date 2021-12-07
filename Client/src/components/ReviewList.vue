<template>
  <div
    @click="goReviewDetail"
    class="container bottom-line mb-3"
  >
    <div class="list-item d-flex align-items-center p-3">
      <div class=" d-flex flex-column ">
        <h3>{{ review.title }}</h3>
        <p class="mb-0"> {{ review.username }} | {{ review.created_at.substr(0,10) }} </p>
      </div>
      <div class="d-flex ms-auto align-self-end">
        <p class="me-1">평점: {{ review.rank }}점 | </p>
        <p>댓글 수: {{ review.reviewcomment_count }}</p>
      </div> 
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
  props:{
    review: {
      type: Object,
    }
  },
  methods:{
    goReviewDetail(){
      return this.$router.push({ name: "ReviewDetail" , query: {data:JSON.stringify({reviewId: this.review.id, movieId:this.review.movie })}})
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