"""depcheck 核心模块（初始失败环境，待修复）。"""

def verify_checksum(content, expected):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def pinned_version(spec):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def lock_bypassed(config):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def source_allowed(url, whitelist):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def verify_signature(pubkey, signature, content):
    """待实现的安全修复入口。"""
    raise NotImplementedError

def resolve_version(spec, locked):
    """待实现的安全修复入口。"""
    raise NotImplementedError
