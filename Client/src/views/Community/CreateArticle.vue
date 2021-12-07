<template>
  <div class="d-flex align-items-center" style="height: 100vh;">
    <div class="container content p-5">
      <h1 class="">게시물 작성</h1>
      <form @submit.prevent="postArticle">
        <div class="mb-3 text-start">
          <label for="title" class="form-label">Title</label>
          <input type="text" class="form-control" id="title" v-model="title" required>
        </div>
        <div class="mb-3 text-start">
          <label for="content" class="form-label">Content</label>
          <textarea name="" class="form-control" id="content" cols="30" rows="10" v-model="content" required></textarea>
        </div>
        <div class="d-flex justify-content-center">
          <button @click="goCommuniuty" type="button" class="btn btn-lg bg-custom text-white me-5">취소하기</button>
          <button  type="submit" class="btn btn-lg bg-custom text-white ">작성하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CreateArticle',
  data(){
    return{
      title: '',
      content: '',
    }
  },
  methods: {
    postArticle() {
      axios.post(`http://localhost:8000/community/articles/create/`, {
        user: this.getUserId,
        title: this.title,
        content: this.content,
      },{
        headers:{
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(response => {
          return this.$router.push({ name: 'ArticleDetail' , query: {data:JSON.stringify({articleId: response.data.id})}})
        })
        .catch(() => {
          alert('잘못된 양식입니다. 다시 한 번 확인해주세요.')
          this.title=''
          this.content=''
        })
    },
    goCommuniuty() {
      this.$router.push({name: 'Community'})
    }
  },
  computed:{
    ...mapGetters([
      'getUserId',
    ])
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