<template>
  <main id="app" class="content">
    <nav class="nav">
      <menu class="nav__controls">
        <div
          v-for="(active, menu) in menus"
          class="nav__label"
          :class="{
            'nav__label--active': active,
            'nav__label--filter': activeFilters[menu].length
          }"
          :key="menu + 0"
          @click="setMenu(menu, active)"
        >
          {{ menu }}
        </div>
        <div class="nav__label nav__label--clear" @click="clearAllFilters">
          Clear all
        </div>
      </menu>
    </nav>

    <transition-group
      name="dropdown"
      tag="section"
      class="dropdown"
      :style="dropdown"
    >
      <menu
        v-for="(options, filter) in filters"
        class="filters"
        v-show="menus[filter]"
        ref="menu"
        :key="filter + 0"
      >
        <div
          v-for="(active, option) in options"
          class="filters__item"
          :class="{ 'filters__item--active': active }"
          @click="setFilter(filter, option)"
          :key="option + 0"
        >
          {{ option }}
        </div>
      </menu>
    </transition-group>

    <transition-group name="question" tag="ul" class="content__list">
      <div
        class="question"
        v-for="question in list"
        :key="question.p_id"
        @click="questionDetail(question.p_id)"
      >
        <div class="question__info">
          <h2 class="question__name">{{ question.p_question }}</h2>
          <blockquote class="question__slogan">
            {{ questionType[question.pt_id] }}
          </blockquote>
        </div>

        <ul class="question__details">
          <label class="question__label">난이도</label>
          <p class="question__level">{{ level[question.pd_id] }}</p>
        </ul>
      </div>
    </transition-group>
  </main>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "WrongAnswerNote",

  data() {
    return {
      questionType: [],
      questionData: [],
      questionCategory: [],
      level: ["", "매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"],
      filters: { type: {}, category: {}, level: {} },
      menus: { type: false, category: false, level: false },
      dropdown: { height: 0 }
    };
  },
  computed: {
    activeFilters() {
      let { type, category, level } = this.filters;
      return {
        type: Object.keys(type).filter(c => type[c]),
        category: Object.keys(category).filter(c => category[c]),
        level: Object.keys(level).filter(c => level[c])
      };
    },

    activeMenu() {
      return Object.keys(this.menus).reduce(
        ($$, set, i) => (this.menus[set] ? i : $$),
        -1
      );
    },
    list() {
      let { type, category, level } = this.activeFilters;
      return this.questionData.filter(({ pt_id, pc_id, pd_id }) => {
        let a = type.length === 0;
        let b = type.length === 0;
        let c = type.length === 0;
        if (
          (type.length === 0 ||
            type.indexOf(this.questionType[pt_id]) !== -1) &&
          (category.length === 0 ||
            category.indexOf(this.questionCategory[pc_id]) !== -1) &&
          (level.length === 0 || level.indexOf(this.level[pd_id]) !== -1)
        ) {
          return true;
        }
      });
    }
  },
  watch: {
    activeMenu(index, from) {
      if (index === from) return;
      this.$nextTick(() => {
        if (!this.$refs.menu || !this.$refs.menu[index]) {
          this.dropdown.height = 0;
        } else {
          this.dropdown.height = `${this.$refs.menu[index].clientHeight +
            16}px`;
        }
      });
    }
  },
  methods: {
    clearFilter(filter, except, active) {
      Object.keys(this.filters[filter]).forEach(option => {
        this.filters[filter][option] = except === option && !active;
      });
    },

    clearAllFilters() {
      Object.keys(this.filters).forEach(this.clearFilter);
    },

    setFilter(filter, option) {
      console.log(filter);
      this.filters[filter][option] = !this.filters[filter][option];
      //   if (filter === "type") {
      //     this.filters[filter][option] = !this.filters[filter][option];
      //   } else {
      //     setTimeout(() => {
      //       this.clearFilter(filter, option, this.filters[filter][option]);
      //     }, 100);
      //   }
    },

    setMenu(menu, active) {
      Object.keys(this.menus).forEach(tab => {
        this.menus[tab] = !active && tab === menu;
      });
    },

    async init() {
      // Category Get
      await axios.get("/api/problems/prob_cate/").then(({ data }) => {
        data.forEach(({ pc_id, pc_value }) => {
          this.$set(this.questionCategory, pc_id, pc_value);
        });
      });

      // Type Get
      await axios.get("/api/problems/prob_type/").then(({ data }) => {
        data.forEach(({ pt_id, pt_value }) => {
          this.$set(this.questionType, pt_id, pt_value);
        });
      });

      // Problems Get
      //   const user_id = this.$store.state["auth"]["userInfo"]["id"];
      //   await axios.get(`/api/xnotes/mynote/${user_id}`).then(({ data }) => {
      //     console.log(data);
      //     this.questionData = data;
      //     data.forEach(({ pt_id, pc_id, pd_id }) => {
      //       // Type, Category
      //       this.$set(this.filters.type, this.questionType[pt_id], false);
      //       this.$set(this.filters.category, this.questionCategory[pc_id], false);
      //       this.$set(this.filters.level, this.level[pd_id], false);
      //     });
      //   });
      //   console.log(this.filters);
      await axios.get("/api/problems/probs/").then(({ data }) => {
        this.questionData = data;
        data.forEach(({ pt_id, pc_id, pd_id }) => {
          // Type, Category
          this.$set(this.filters.type, this.questionType[pt_id], false);
          this.$set(this.filters.category, this.questionCategory[pc_id], false);
          this.$set(this.filters.level, this.level[pd_id], false);
        });
      });
      console.log(this.filters);
    }
  },

  beforeMount() {
    this.init();
  }
};
</script>

<style lang="scss" src="@/components/Question/CategoryList.scss" scoped></style>
