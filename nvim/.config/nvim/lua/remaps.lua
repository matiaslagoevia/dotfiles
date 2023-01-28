-- Use space as the leader key
vim.g.mapleader = ' '

function map(mode, lhs, rhs, opts)
    local options = { noremap = true }
    if opts then
        options = vim.tbl_extend('force', options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

-- Pane movement
map("n", "<Leader>l", "<C-W><C-L>", { silent = true })
map("n", "<Leader>h", "<C-W><C-H>", { silent = true })
map("n", "<Leader>k", "<C-W><C-K>", { silent = true })
map("n", "<Leader>j", "<C-W><C-J>", { silent = true })

