<template>
  <main id="app" class="main-container">
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
          {{ menuName[menu] }}
        </div>
        <div class="nav__label nav__label--clear" @click="clearAllFilters">
          초기화
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
    <noteCard
      :list="list"
      :questionType="questionType"
      :questionCategory="questionCategory"
      :level="level"
      @deleteMynote="deleteMynote"
    />
  </main>
</template>

<script>
import axios from "@/api/api.service.js";
import noteCard from "@/components/Note/noteCard.vue";

export default {
  name: "IT_Note",
  components: {
    noteCard
  },

  data() {
    return {
      questionType: [],
      questionData: [],
      questionCategory: [],
      level: ["", "매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"],
      filters: { type: {}, category: {}, level: {} },
      menus: { type: false, category: false, level: false },
      menuName: { type: "문제유형", category: "문제주제", level: "난이도" },
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
      return this.questionData.filter(({ problems }) => {
        let a = type.length === 0;
        let b = type.length === 0;
        let c = type.length === 0;
        if (
          (type.length === 0 ||
            type.indexOf(this.questionType[problems.pt_id]) !== -1) &&
          (category.length === 0 ||
            category.indexOf(this.questionCategory[problems.pc_id]) !== -1) &&
          (level.length === 0 ||
            level.indexOf(this.level[problems.pd_id]) !== -1)
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
    deleteMynote(myNote) {
      this.questionData = myNote;
    },
    clearFilter(filter, except, active) {
      Object.keys(this.filters[filter]).forEach(option => {
        this.filters[filter][option] = except === option && !active;
      });
    },

    clearAllFilters() {
      Object.keys(this.filters).forEach(this.clearFilter);
    },

    setFilter(filter, option) {
      this.filters[filter][option] = !this.filters[filter][option];
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
      const user_id = this.$store.state["auth"]["userInfo"]["id"];
      await axios.get(`/api/myprobs/myprob/${user_id}`).then(({ data }) => {
        this.questionData = data;

        data.forEach(({ problems }) => {
          // Type, Category
          this.$set(
            this.filters.type,
            this.questionType[problems.pt_id],
            false
          );
          this.$set(
            this.filters.category,
            this.questionCategory[problems.pc_id],
            false
          );
          this.$set(this.filters.level, this.level[problems.pd_id], false);
        });
      });
    }
  },

  beforeMount() {
    this.init();
  }
};
</script>

<style lang="scss" scopred>
.main-container {
  width: 100%;
  max-width: 500px;
  height: 100%;
  margin: 0 auto;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  white-space: nowrap;
  margin: 0 1rem;
  padding: 2rem 0.5rem 1rem;
  border-bottom: 1px solid #c5d0d1;

  &__controls {
    display: flex;
  }

  &__label {
    font-family: "Recipekorea";
    position: relative;
    margin-left: 1rem;
    text-transform: capitalize;
    cursor: pointer;

    &::after {
      content: "\00d7";
      display: inline-block;
      color: transparent;
      width: 0.5rem;
      font-weight: 400;
      transform: scale(0);
      transition: transform 150ms ease-in-out;
    }

    &--clear {
      color: #f68185;
      opacity: 0;
      transform: translate3d(-25%, 0, 0);
      pointer-events: none;
      transition: all 275ms ease-in-out;
    }

    &--filter ~ &--clear {
      opacity: 1;
      transform: translate3d(0, 0, 0);
      pointer-events: auto;
    }

    &--filter::after,
    &--active::after {
      transform: scale(1);
    }

    &--filter::after {
      content: "\2022";
      color: #46d2c4;
    }

    &--active::after {
      content: "\00d7";
      color: #f68185;
    }
  }
}

.dropdown {
  position: relative;
  height: 0;
  overflow: hidden;
  transition: height 350ms;

  &::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1rem;
    background-image: linear-gradient(to top, white, rgba(white, 0));
  }

  &-enter,
  &-leave-to {
    opacity: 0;
  }

  &-leave,
  &-enter-to {
    opacity: 1;
  }

  &-enter-active,
  &-leave-active {
    position: absolute;
    width: 100%;
    transition: opacity 200ms ease-in-out;
  }

  &-enter-active {
    transition-delay: 100ms;
  }
}

.filters {
  padding: 0 1rem;
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;

  &__item {
    font-family: "Recipekorea";
    margin-top: 0.5rem;
    margin-right: 0.5rem;
    padding: 0.25rem 0.5rem;
    border: 1px solid #c5d0d1;
    border-radius: 6px;
    font-size: 0.8rem;
    line-height: 1.35;
    cursor: pointer;
    transition: all 275ms;

    &:hover {
      border-color: #379a93;
    }

    &--active {
      color: white;
      border-color: #379a93;
      background-color: #379a93;
    }
  }
}

@font-face {
  font-family: "godoMaum";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/godoMaum.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "Recipekorea";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Recipekorea.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "CookieRunOTF-Bold";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/CookieRunOTF-Bold00.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "MapoPeacefull";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoPeacefullA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>
