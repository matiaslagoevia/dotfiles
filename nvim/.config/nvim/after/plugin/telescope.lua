local builtin = require('telescope.builtin')

-- Below, "project" refers to the pwd where neovim was launched
-- It may not reflect the open buffer's directory

-- Find in all project files
vim.keymap.set('n', '<leader>pf', builtin.find_files, {})
-- Find in all git-tracked project files
vim.keymap.set('n', '<C-p>', builtin.git_files, {})
-- Perform (rip)grep search on all project files
vim.keymap.set('n', '<leader>ps', function()
    builtin.grep_string({ search = vim.fn.input("(rip)grep > ") })
end)