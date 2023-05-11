{ pkgs, ... }:

{
  packages = with pkgs; [
    git
    python310Packages.python-lsp-server
    python310Packages.python-lsp-black
    python310Packages.pylsp-mypy
    black
  ];

  languages.python = {
    enable = true;
    poetry = {
      enable = true;
    };
  };

  languages.typescript.enable = true;
  languages.javascript.enable = true;

  services.postgres = {
    enable = true;
    initialScript = ''
      CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'postgres';
    '';
    initialDatabases = [
      { name = "backend"; }
    ];
  };
}
