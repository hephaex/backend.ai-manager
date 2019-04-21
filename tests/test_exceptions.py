import json

<<<<<<< HEAD
from backend.ai.gateway.exceptions import Backend.AiError, Backend.AiAgentError
from backend.ai.utils import odict


def test_backend.ai_error_obj():
    backend.ai_err = Backend.AiError()
    assert backend.ai_err.args == (backend.ai_err.status_code, backend.ai_err.reason,
                              backend.ai_err.error_type)
    assert backend.ai_err.body == json.dumps(odict(
        ('type', backend.ai_err.error_type), ('title', backend.ai_err.error_title)
    )).encode()

    extra_msg = '!@#$'
    backend.ai_err = Backend.AiError(extra_msg)
    assert extra_msg in backend.ai_err.error_title


def test_backend.ai_agent_error_obj():
    agt_err = Backend.AiAgentError('timeout')
=======
from ai.backend.gateway.exceptions import BackendError, BackendAgentError
from ai.backend.common.utils import odict


def test_backend_error_obj():
    eobj = BackendError()
    assert eobj.args == (eobj.status_code, eobj.reason, eobj.error_type)
    assert eobj.body == json.dumps(odict(
        ('type', eobj.error_type), ('title', eobj.error_title)
    )).encode()

    extra_msg = '!@#$'
    eobj = BackendError(extra_msg)
    assert extra_msg in eobj.error_title


def test_backend_agent_error_obj():
    eobj = BackendAgentError('timeout')
>>>>>>> c2bb79a19c0574845ab66cc5f3c3402c9833ea34

    assert eobj.args == (eobj.status_code, eobj.reason,
                         eobj.error_type, eobj.agent_error_type)
    assert eobj.body == json.dumps(odict(
        ('type', eobj.error_type),
        ('title', eobj.error_title),
        ('agent-details', odict(
            ('type', eobj.agent_error_type),
            ('title', eobj.agent_error_title),
        )),
    )).encode()
