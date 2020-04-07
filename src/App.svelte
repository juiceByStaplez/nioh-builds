<script>
  export const skills = [
    'axe',
    'dual-swords',
    'hatchets',
    'kusarigami',
    'magic',
    'ninjutsu',
    'odachi',
    'samurai',
    'shiftling',
    'spear',
    'switchglaive',
    'sword',
    'tonfa',
  ]

  let selectedSkill = ''

  $: selectedSkill

  function handleClick(evt) {
    selectedSkill = evt.target.value
  }
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<main>
  <nav class="flex flex-col">
    <ul class="list-reset flex justify-between">
      {#each skills as skill}
        <li>
          <button
            class="capitalize"
            value={skill}
            on:click={e => handleClick(e)}>
            {skill}
          </button>
        </li>
      {/each}
    </ul>
  </nav>
  <section id="skilltree">{selectedSkill}</section>
</main>
