<template>
  <div class="mt-3">
    <div class="d-flex justify-content-between align-items-center">
      <p>작성자: {{ comment.username }} | 
        <span v-if="comment.created_at.substr(0,19) === comment.updated_at.substr(0,19)">{{ comment.created_at.substr(0,10)}}</span>
        <span v-else>{{ comment.updated_at.substr(0,10)}} (수정됨)</span>
      </p>
      <div class="d-flex justify-content-between align-items-center">
        <button
          v-if="isMine && !editNow"
          @click="toggleMovieComment"
          class="btn bg-custom text-white py-1 mx-1"
        >
        수정
        </button>
        <button 
          v-else-if="isMine && editNow"
          @click="editMovieComment"
          class="btn bg-custom text-white py-1 mx-1"
        >
          완료
        </button>
        <button 
          v-if="isMine"
          @click="deleteMovieComment"
          class="btn bg-custom text-white py-1 mx-1"
        >
        삭제
        </button>
      </div>
    </div>

    <input
      class="form-control"
      @keyup.enter="editMovieComment"
      v-if="editNow && isMine" 
      type="text" 
      v-model="editComment"
    >
    <p v-else>{{ comment.content }}</p>
    <hr>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object,
    }
  },
  data(){
    return{
      editComment: this.comment.content,
      editNow: false,
    }
  },
  methods:{
    deleteMovieComment(){
      this.$store.dispatch('deleteMovieComment', this.comment)
    },
    toggleMovieComment(){
      this.editNow = !this.editNow
    },
    editMovieComment(){
      this.editNow = !this.editNow
      this.$store.dispatch('editMovieComment', {
        ...this.comment,
        content: this.editComment,
      })
    }
  },
  computed:{
    ...mapGetters([
      'getUserId'
    ]),
    isMine() {
      if(this.getUserId === this.comment.user){
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>
  .bg-custom{
    background-color: rgb(103,42,66);
  }
</style>