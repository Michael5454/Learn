<template>
    <div>
      <input placeholder="请输入英文名" @input="input" v-model="name_en">
      <p>中文名：{{ name_cn }}</p>
      <p>邮箱：{{ email }}</p>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      name_en: "",
      name_cn: "",
      email: "",
      emps:[
        {"name_en": "michael","name_cn": "尚亚辉","email": "michael.shang@sanofi.com"},
        {"name_en": "forrest","name_cn": "苏永佳","email": "forrest.su@sanofi.com"},
      ]
    }
  },
  async mounted () {
    var that = this
    that.getEmps()
  },
  methods: {
    async getEmps () {
      var that = this
      console.log("我活了")
      axios.get('http://127.0.0.1:5000/getEmps')
        .then(response => {
          console.log(response.data)
          that.emps = response.data;
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    async input(){
      var that = this
      that.name_cn=""
      that.email=""
      that.emps.forEach(emp => {
        if (that.name_en.toUpperCase()==emp["name_en"].toUpperCase()) {
          that.name_cn=emp["name_cn"]
          that.email=emp["email"]
        }
      });
    }
  }
}
</script>

