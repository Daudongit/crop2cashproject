<template>
    <section class="content">
        <navbar />
        <!-- <main-content/> -->
<div class="container" style="margin-top:20px">
<div class="row">
    <div class="col-md-12">
      <div class="card support-pane-card">
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 class="card-title mb-0">  Item List </h4>
            <div class="btn-toolbar mb-0 d-sm-block" role="toolbar" 
                aria-label="Toolbar with button groups">
            </div>
          </div>
  
          <div class="table-responsive support-pane no-wrap">
            <table class="table">
              <thead>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr  v-for="(item, key) in items" :key="key">
                  <td>{{item.name}}</td>
                  <td>{{item.description}}</td>
                  <td>{{item.price}}</td>
                  <td>
                      <button class="btn btn-primary btn-xs" @click="showDetail(item.id)">
                        <i class="icon-eye"></i> Details
                      </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="d-flex float-right align-items-center mt-4">
          </div>
        </div>
      </div>
    </div>
</div>
</div>
    </section>
</template>
<script>
import DefaultLayout from '../layouts/DefaultLayout.vue'
import Navigation from '../layouts/Navigation.vue'
import MainContent from '../layouts/MainContent.vue'
import Navbar from '../components/Navbar.vue'
import axios from 'axios'

export default {
    name:'Dashboard',
    middleware: 'auth',
    components:{MainContent,Navbar},
    data:()=>({
      items:null
    }),
    async created(){
      try {
        const  {data}  = await axios.get('/api/items')
        this.items = data.data
      } catch (e) {}

        // this.$emit('update:layout',DefaultLayout)
    },
    methods:{
      showDetail(item_id){
        
        console.log(item_id)
      }
    }
}
</script>